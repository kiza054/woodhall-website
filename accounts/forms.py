from django import forms
from accounts.models import User, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

SECTION = [
    ('Beavers', 'Beavers'),
    ('Cubs', 'Cubs'),
    ('Scouts', 'Scouts'),
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    section = forms.ChoiceField(label='Childs Section', choices=SECTION, widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'section']

class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
        }
    ))

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    section = forms.ChoiceField(label='Childs Section', choices=SECTION, widget=forms.RadioSelect)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'section']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']