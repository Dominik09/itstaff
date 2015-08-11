# coding: utf-8
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/files/media')
# Create your models here.
class Sheet(models.Model):
    class Meta():
        db_table = "sheet"
    title = models.CharField(max_length = 300)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default = 0)
    image = models.ImageField(upload_to="", null = True, blank = True)
    def __str__(self):
        return self.title
class Comments(models.Model):
    class Meta():
        db_table = "comments"
    com_text = models.TextField(verbose_name="Текст комментария:")
    com_sheet = models.ForeignKey(Sheet)