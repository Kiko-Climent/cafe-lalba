from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Define the opening hour for bookings
OPENING_HOUR = datetime.strptime("18:00", "%H:%M").time()


# Booking model for reservations
class Booking(models.Model):
    name = models.CharField(max_length=150)
    num_people = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField(default=OPENING_HOUR)
    end_time = models.TimeField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = (
                datetime.combine(self.date, self.start_time) + timedelta(
                    hours=1)).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
