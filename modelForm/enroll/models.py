from django.db import models

# Create your models here.
class WebUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)    
    password = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("WebUser")
        verbose_name_plural = ("WebUsers")

    def __str__(self):
        return self.name

