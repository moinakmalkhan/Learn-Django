from django.dispatch import Signal,receiver

notification = Signal(['request', 'user'])

@receiver(notification)
def show_notification(sender, **kwargs):
    print("------------signal start----------")
    print(f"sender : {sender}" )
    print(f"Kwargs : {kwargs}")
    print("------------signal end----------")

