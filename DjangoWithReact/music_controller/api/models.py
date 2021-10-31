from django.db import models
import random
import string

def genreate_random_code():
    length = 6
    while True:
        code = "".join(random.choices(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code =  models.CharField(max_length=10,default=genreate_random_code,unique=True)
    host = models.CharField(max_length=80,unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    vote_to_skip = models.IntegerField(null=False,default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.code