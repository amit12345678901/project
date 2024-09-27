from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    message = models.CharField(max_length=200)  # Changed 'Message' to 'message' for consistency

    def __str__(self):
        return f"{self.name} - {self.email}"