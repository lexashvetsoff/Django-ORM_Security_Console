import datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_datetime(localtime):
    return datetime.datetime(localtime.year,
                            localtime.month,
                            localtime.day,
                            localtime.hour,
                            localtime.minute,
                            localtime.second)


def get_duration(visit):
    if visit.leaved_at:
        start = get_datetime(visit.entered_at)
        closed = get_datetime(visit.leaved_at)
        visit_time = closed - start
    else:
        now = get_datetime(localtime())
        then = get_datetime(visit.entered_at)
        visit_time = now - then
    return visit_time


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int((duration.total_seconds() % 3600) // 60)
    return f'{hours} ч. {minutes} мин.'


def get_visit_time(visit):
    # возвращает время в минутах
    visit_time = get_duration(visit)
    return int(visit_time.total_seconds() // 60)


def is_visit_long(visit, minutes=60):
    return get_visit_time(visit) >= minutes


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    # Программируем здесь

    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        duration = get_duration(passcard_visit)
        visit = {
                    'entered_at': passcard_visit.entered_at,
                    'duration': format_duration(duration),
                    'is_strange': is_visit_long(passcard_visit),
                }
        this_passcard_visits.append(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
