from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Review
from django.forms import ModelForm, Textarea, Select, TextInput, FileInput
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  


# https://docs.djangoproject.com/en/4.1/ref/forms/validation/


class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':('form-control')})
        self.fields['password1'].widget.attrs.update({'class':('form-control')})        
        self.fields['password2'].widget.attrs.update({'class':('form-control')})
        self.fields['email'].widget.attrs.update({'class':('form-control')})
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Такой юзер уже существует👥")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Такой email уже существует📧")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Пароли не совпадают")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  


class SigninForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':('form-control')})
        self.fields['password'].widget.attrs.update({'class':('form-control')})       



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["task", "stars", "image"]
        widgets = {
            "task": Textarea(attrs={
                'class': 'form-control',
            }),
            "stars": Select(choices=[(str(star), star) for star in range(1, 6)], attrs={
                'class': 'form-control'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
            }),
        }