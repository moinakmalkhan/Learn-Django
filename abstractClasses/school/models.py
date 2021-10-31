from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("name")


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract =True
class Student(Person):
    fee = models.IntegerField()
    objects = models.Manager()
    students = CustomManager()

class Teacher(Person):
    salary = models.IntegerField()



