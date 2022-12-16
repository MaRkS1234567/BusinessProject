from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Review
from django.forms import ModelForm, Textarea, Select, TextInput, FileInput

class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':('form-control')})
        self.fields['password1'].widget.attrs.update({'class':('form-control')})        
        self.fields['password2'].widget.attrs.update({'class':('form-control')})

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