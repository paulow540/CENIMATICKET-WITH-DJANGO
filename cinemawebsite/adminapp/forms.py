from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from Ecommance.adminapp.models import Product_table

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required="false", help_text ='Optional')
    last_name = forms.CharField(max_length=30, required="false", help_text ='Optional')
    email = forms.EmailField(max_length=30, required="false", help_text ='Enter a valid email address ')
