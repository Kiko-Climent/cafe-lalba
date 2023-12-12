from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    notes = models.TextField(max_length=500)
    responded = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    admin_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
