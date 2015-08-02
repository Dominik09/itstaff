from django.db import models
from django.contrib.auth.models import AbstractUser

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

class User(AbstractUser):

	birth_date = models.DateField(
		null = True,
		blank = True,
		verbose_name = 'Дата рождения',
	)