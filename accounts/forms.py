from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import \
    PasswordResetForm as PasswordResetFormCore
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile, User
from accounts.tasks import send_mail

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

PERMISSION = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    section = forms.ChoiceField(label='Childs Section', choices=SECTION, help_text='Please select the section that your child currently attends.')
    second_section = forms.ChoiceField(label='Childs Second Section', choices=SECOND_SECTION, 
        help_text='Please only use this if you have a child in another section, otherwise select "Not Applicable".')
    photo_permission = forms.ChoiceField(label='Photographic Permission', choices=PERMISSION, help_text='Please let us know whether we have your permission to share your childs photos on this website.')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'section', 'second_section', 'photo_permission']

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
    photo_permission = forms.ChoiceField(label='Photographic Permission', choices=PERMISSION, help_text='Please let us know whether we have your permission to share your childs photos on this website.')

    class Meta:
        model = User
        fields = ['username', 'email', 'section', 'second_section', 'photo_permission']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PasswordResetForm(PasswordResetFormCore):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Email'
        }
    ))

    def send_mail(self, subject_template_name, email_template_name, context, 
                  from_email, to_email, html_email_template_name=None):
        context['user'] = context['user'].id

        send_mail.delay(subject_template_name=subject_template_name, 
                        email_template_name=email_template_name,
                        context=context, from_email=from_email, to_email=to_email,
                        html_email_template_name=html_email_template_name)