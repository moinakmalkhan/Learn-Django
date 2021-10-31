from django.db import models
from django.db.models import manager
from django.db import models
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("name")
    def get_roll_range(self,from_,to):
        return super().get_queryset().filter(roll__range=(from_,to))
