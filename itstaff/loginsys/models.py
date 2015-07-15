from django.db import models
from django.contrib.auth.models import AbstractUser

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

# Переопределяем базовый класс пользователя
class User(AbstractUser):
    # Дата рождения
    birth_date = models.DateField(null = True, blank = True)
    # Специализация пользователя
    specialization = models.CharField(max_length = 50)
    # "о себе"
    about_youself = models.TextField(verbose_name = 'Напишите о себе')
    # Пол
    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Женщна')
    )
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, default = 'Пол')
    # Категория пользователя
    CATEGORIES = (
        ('UN', 'Unverificated'),
        ('NEW', 'Newbie'),
        ('SP', 'Specialist')
    )
    category = models.CharField(max_length = 3, choices = CATEGORIES, default = 'UN')