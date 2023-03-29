from django.db import models
import time
import datetime
from django.utils import timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

def finding_time_spent_in_storage(visit):
    time_when_enter = timezone.localtime(visit.entered_at)
    time_when_leaved = timezone.localtime(visit.leaved_at)
    spent_time = time_when_leaved - time_when_enter
    spent_time_in_sec = spent_time.total_seconds()
    return spent_time_in_sec

def format_time(duration):
    hours = int(duration // 3600)
    min = int(duration % 3600 // 60)
    sec = int(duration % 60)
    time_spent = f'{hours}:{min}'
    print(time_spent)
    return time_spent

def is_visit_long(duration, sec=3600):
    return duration > sec


