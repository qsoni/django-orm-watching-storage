from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.models import format_time
from datacenter.models import finding_time_spent_in_storage
from datacenter.models import is_visit_long

def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = [

    ]
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered_at = visit.entered_at
        finding_time_spent_in_storage(visit)
        duration = finding_time_spent_in_storage(visit)
        time_spent = format_time(duration)
        is_starange = is_visit_long(duration)
        this_passcard_visits.append({'entered_at': entered_at,
                                     'duration': time_spent,
                                     'is_strange': is_starange})
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
