from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    message = models.CharField(max_length=200)  # Changed 'Message' to 'message' for consistency

    def __str__(self):
        return f"{self.name} - {self.email}"


class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('1', 'Post-Trauma'),
        ('2', 'Post-Recovery'),
        ('3', 'Migraines'),
        ('4', 'Chronic Pains'),
    ]
    
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service}"