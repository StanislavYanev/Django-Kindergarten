from django.db import models
from user.models import Teacher


class ChildrenGames(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='events/', blank=True)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    person_responsible = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    event_games = models.ManyToManyField(ChildrenGames)
    description = models.TextField()

    def __str__(self):
        return self.name


