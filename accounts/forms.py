from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  ]


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
