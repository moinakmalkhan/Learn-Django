from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def success(sender,request, user, **kwargs):
    print("--------------------------------------")
    print("Logged in signal ---------Intro-------")
    print(f"Sender {sender}")
    print(f"Requset {request}")
    print(f"User {user}")
    print(f"kwargs {kwargs}")
# user_logged_in.connect(success, sender=User)