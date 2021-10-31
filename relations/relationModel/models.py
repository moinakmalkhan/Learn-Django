from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Page(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=50)
    publish_date = models.DateField()


class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=70)
    duration = models.CharField(max_length=50)

    def sing_by(self):
        print(self.user.all())
        return ", ".join([str(s) for s in self.user.all()])
