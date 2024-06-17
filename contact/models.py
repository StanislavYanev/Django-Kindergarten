from django.db import models

# Create your models here.

class Contact(models.Model):
    topic = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.last_name} -{self.topic}"