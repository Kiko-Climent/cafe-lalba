from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=150)
    num_people = models.IntegerField()
    date = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

