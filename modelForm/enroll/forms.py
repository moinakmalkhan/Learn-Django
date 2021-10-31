from django.core import validators
from django import forms
from .models import WebUser


class WebUserForm(forms.ModelForm):

    class Meta:
        model = WebUser
        fields = ("name", "email", "password")
        labels = {"name": "Enter You name: ", "email": "Enter your email: ",
                  "password": "Enter your Password: "}
        widgets = {"password": forms.PasswordInput(
            attrs={'class': 'form-control'})}

    # def __init__(self, *args, **kwargs):
    #     super(WebUserForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
