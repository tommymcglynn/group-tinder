from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    STEREOTYPES = (
        (0, 'Jock'),
        (1, 'Hippie'),
        (2, 'Bro'),
        (3, 'Diva'),
        (4, 'Bookworm'),
        (5, 'Techie'),
        (6, 'Dancer'),
        (7, 'Emo'),
    )
    user = models.OneToOneField(User, primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    stereotype = models.IntegerField(choices=STEREOTYPES)
