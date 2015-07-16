from django.db import models
from django.contrib.auth.models import AbstractUser

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

# Переопределяем базовый класс пользователя
class User(AbstractUser):

    # Дата рождения
    birth_date = models.DateField(
        null = True,
        blank = True,
        verbose_name = 'Дата рождения')

    # Специализация пользователя
    specialization = models.CharField(
        null = True,
        blank = True,
        max_length = 50,
        verbose_name = 'На чем вы специализируетесь?'
    )

    # "о себе"
    about_youself = models.TextField(
        null = True,
        blank = True,
        verbose_name = 'Напишите о себе'
    )

    # Категория пользователя
    CATEGORIES = (
        ('UN', 'Unverificated'),
        ('NEW', 'Newbie'),
        ('SP', 'Specialist')
    )
    category = models.CharField(
        max_length = 3,
        choices = CATEGORIES,
        default = 'UN',
        verbose_name = 'Категория',
    )

    # Университет
    university = models.CharField(
        null = True,
        blank = True,
        max_length = 100,
        verbose_name = 'Университет',
    )

    # Кружки
    clubs = models.CharField(
        null = True,
        blank = True,
        max_length = 100,
        verbose_name = 'Посещали ли вы кружки?'
    )

    # Портфолио


class Portfolio(models.Model):

    class Meta():
        db_table = 'portfolio'

    # Чье портфолио
    user = models.ForeignKey(User)

    # Скрин
    screenshot = models.ImageField(
        verbose_name = 'Скриншот',
    )

    # Описание проекта
    about = models.TextField(
        verbose_name = 'Расскажите о проекте',
    )

    # Ссылка на проект
    link = models.URLField(
        null = True,
        blank = True,
        verbose_name = 'Ссылка на проект',
    )