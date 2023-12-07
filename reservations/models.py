from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Define la hora de apertura como una variable global
OPENING_HOUR = datetime.strptime("18:00", "%H:%M").time()

class Booking(models.Model):
    name = models.CharField(max_length=150)
    num_people = models.IntegerField()
    date = models.DateField()
    
    # Usa la variable OPENING_HOUR como valor por defecto
    start_time = models.TimeField(default=OPENING_HOUR)

    # Define el valor por defecto para end_time directamente en el campo
    end_time = models.TimeField(default=(datetime.combine(datetime.now().date(), OPENING_HOUR) + timedelta(hours=2)).time())
    
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
