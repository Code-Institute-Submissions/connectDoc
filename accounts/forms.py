from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UniqueUserEmailField(forms.EmailField):
    
    """
    An EmailField which only is valid if no user has that email.
    """
    
    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.Objects.get(email = value)
            raise forms.ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass



class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    email= UniqueUserEmailField(required = True, label = "Email address")

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'password1', 'password2', 'email', ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        
        return user
    
    
    
