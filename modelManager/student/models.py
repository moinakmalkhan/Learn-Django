from django.db import models
from .manager import CustomManager
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    students = CustomManager()
    objects = models.Manager()
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name


