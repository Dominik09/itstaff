from django.db import models
from django.contrib.auth.models import AbstractUser

AbstractUser._meta.get_field('email')._unique = True

class User(models.Model):
    class Meta():
        db_table = 'user'

    birth_date = models.DateTimeField(null = True, blank = True)
    specialization = models.CharField(max_length = 50)
    about_youself = models.TextField(verbose_name = 'Напишите о себе')

    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Женщна')
    )
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, default = 'Пол')

    CATEGORIES = (
        ('UN', 'Unverificated'),
        ('NEW', 'Newbie'),
        ('SP', 'Specialist')
    )
    category = models.CharField(max_length = 3, choices = CATEGORIES, default = 'UN')