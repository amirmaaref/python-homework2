from django.db import models
import datetime

'''
contact

phone_number

call_history
'''

'''
orm

object relational mapping
'''

'''
ForeignKey!


'''


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    profile_photo = models.CharField(max_length=255, blank=True, null=True)
    birth_day = models.DateField(null=True, blank=True)


class PhoneNumber(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default='Mobile')
    number = models.CharField(max_length=50, blank=False, null=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class CallHistory(models.Model):
    class HistoryType(models.TextChoices):
        SENT = 'SE', 'Sent'
        REJECTED = 'RJ', 'Rejected'
        RECEIVED = 'RC', 'Received'
        MISSED = 'MS', 'Missed'

    history_type = models.CharField(
        max_length=2,
        choices=HistoryType.choices
    )

    number = models.CharField(max_length=50, blank=False, null=False)
    history_date_time = models.DateTimeField(default=datetime.datetime.now)
    history_time = models.IntegerField(default=0)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
