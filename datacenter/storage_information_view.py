from datacenter import functions as fn

from django.utils.timezone import localtime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    not_leave_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for not_leave_visit in not_leave_visits:
        duration = fn.get_duration(not_leave_visit)
        non_closed_visit = {'who_entered': not_leave_visit.passcard,
                            'entered_at': localtime(not_leave_visit.entered_at),
                            'duration': fn.format_duration(duration),
                           }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
