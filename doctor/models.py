from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    nid = models.IntegerField()
    registration_no = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)