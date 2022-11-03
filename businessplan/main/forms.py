from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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