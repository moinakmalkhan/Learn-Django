from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","fee"]
@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","salary"]

