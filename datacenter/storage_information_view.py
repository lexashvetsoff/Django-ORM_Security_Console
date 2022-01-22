import datetime

from django.utils.timezone import localtime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def get_datetime(localtime):
    return datetime.datetime(localtime.year,
                            localtime.month,
                            localtime.day,
                            localtime.hour,
                            localtime.minute,
                            localtime.second)


def get_duration(visit):
    now = get_datetime(localtime())
    then = get_datetime(visit.entered_at)
    return now - then


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int((duration.total_seconds() % 3600) // 60)
    return f'{hours} ч. {minutes} мин.'


def storage_information_view(request):
    # Программируем здесь

    not_leave_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for not_leave_visit in not_leave_visits:
        duration = get_duration(not_leave_visit)
        non_closed_visit = {'who_entered': not_leave_visit.passcard,
                            'entered_at': localtime(not_leave_visit.entered_at),
                            'duration': format_duration(duration),
                           }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
