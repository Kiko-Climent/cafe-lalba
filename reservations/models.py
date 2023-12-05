from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    client_name = models.CharField(max_length=150)
    num_people = models.IntegerField()
    date_time = models.DateTimeField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name