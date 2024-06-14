
from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    age = models.IntegerField(blank=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

