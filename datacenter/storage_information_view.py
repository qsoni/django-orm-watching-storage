from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_time
from datacenter.models import finding_time_spent_in_storage

def storage_information_view(request):

    non_closed_visits = [

    ]
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for non_closed_visit in not_leaved:
        owner_name = non_closed_visit.passcard.owner_name
        when_entered = non_closed_visit.entered_at
        time_spent_in_sec = finding_time_spent_in_storage(non_closed_visit)
        time_spent = format_time(time_spent_in_sec)
        non_closed_visits.append({'who_entered': owner_name,
                                  'entered_at': when_entered,
                                  'duration': time_spent})
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

