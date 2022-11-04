from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import Profile, User

SECTION = [
    ('Beavers', 'Beavers'),
    ('Cubs', 'Cubs'),
    ('Scouts', 'Scouts'),
]

SECOND_SECTION = [
    ('Beavers', 'Beavers'),
    ('Cubs', 'Cubs'),
    ('Scouts', 'Scouts'),
    ('N/A', 'Not Applicable')
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    section = forms.ChoiceField(label='Childs Section', choices=SECTION, help_text='Please select the section that your child currently attends.')
    second_section = forms.ChoiceField(label='Childs Second Section', choices=SECOND_SECTION, 
        help_text='Please only use this if you have a child in another section, otherwise select "Not Applicable".')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'section', 'second_section']

class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
        }
    ))

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    section = forms.ChoiceField(label='Childs Section', choices=SECTION, help_text='Please select the section that your child currently attends.')
    second_section = forms.ChoiceField(label='Childs Second Section', choices=SECOND_SECTION, 
        help_text='Please only use this if you have a child in another section, otherwise select "Not Applicable".')

    class Meta:
        model = User
        fields = ['username', 'email', 'section', 'second_section']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']