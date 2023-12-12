from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.email  # Muestra el email como representación del modelo en el admin
