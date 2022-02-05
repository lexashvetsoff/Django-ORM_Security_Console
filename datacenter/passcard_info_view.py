from datacenter import functions as fn

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        duration = fn.get_duration(passcard_visit)
        visit = {
                    'entered_at': passcard_visit.entered_at,
                    'duration': fn.format_duration(duration),
                    'is_strange': fn.is_visit_long(passcard_visit),
                }
        this_passcard_visits.append(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
