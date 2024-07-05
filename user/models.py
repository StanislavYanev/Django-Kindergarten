from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from guardian.shortcuts import assign_perm


class ChildrenGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


#This will be only for Admin access
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    picture = models.ImageField(upload_to='teacher_pictures', blank=True)
    phone_number = models.CharField(max_length=100)
    experience = models.DecimalField(decimal_places=0, max_digits=4,validators=[MinValueValidator(0.00, message="Value must be positive.")])
    short_description = models.TextField()
    children_group = models.ManyToManyField(ChildrenGroup)

    class Meta:
        permissions = [
            ("can_view_admin_panel", "Can view admin panel"),
        ]

    def __str__(self):
        return f"{self.name}  {self.last_name}"

#This will be for User-Teacher access
class Parent(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}  {self.last_name}"

#This will be for User-Teacher access
class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='child_pictures', blank=True)
    children_group = models.ForeignKey(ChildrenGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}  {self.last_name}"\


