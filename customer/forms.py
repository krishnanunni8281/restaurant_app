from django.contrib.auth.forms import UserCreationForm
from customer.models import User
from django import forms
from customer.models import Orders


class UserRegistration(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","role"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),

            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # "phone":forms.TextInput(attrs={"class":"form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            # "password2": forms.PasswordInput(attrs={"class": "form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control"})
        }








