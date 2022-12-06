from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import \
    PasswordResetForm as PasswordResetFormCore
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile, User
from accounts.tasks import send_mail

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    section = forms.ChoiceField(
        choices = (
            ('Beavers', 'Beavers'),
            ('Cubs', 'Cubs'),
            ('Scouts', 'Scouts')
        ),
        label='Childs Section', widget=forms.RadioSelect(),
        help_text='Please select the section that your child currently attends.')

    second_section = forms.ChoiceField(
        choices = (
            ('Beavers', 'Beavers'),
            ('Cubs', 'Cubs'),
            ('Scouts', 'Scouts'),
            ('N/A', 'Not Applicable')
        ),
        label='Childs Second Section', widget=forms.RadioSelect(),
        help_text='Please only use this if you have a child in another section, otherwise select "Not Applicable".')

    photo_permission = forms.ChoiceField(
        choices = (
            ('Yes', 'Yes'),
            ('No', 'No')
        ),
        label='Photographic Permission', widget=forms.RadioSelect(),
        help_text='Please let us know whether we have your permission to share your childs photos on this website.')

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
        }
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('username', 'Username:'),
            PrependedText('email', 'Email:'),
            'section',
            'second_section',
            'photo_permission',
            'captcha',
            HTML('<button class="btn btn-outline-info" type="submit">'
                '<i class="fa-duotone fa-user-plus"></i> Sign Up'
                '</button>')
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'section', 'second_section', 'photo_permission', 'captcha']

class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
        }
    ))

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    section = forms.ChoiceField(
        choices = (
            ('Beavers', 'Beavers'),
            ('Cubs', 'Cubs'),
            ('Scouts', 'Scouts')
        ),
        label='Childs Section', widget=forms.RadioSelect(),
        help_text='Please select the section that your child currently attends.')

    second_section = forms.ChoiceField(
        choices = (
            ('Beavers', 'Beavers'),
            ('Cubs', 'Cubs'),
            ('Scouts', 'Scouts'),
            ('N/A', 'Not Applicable')
        ),
        label='Childs Second Section', widget=forms.RadioSelect(),
        help_text='Please only use this if you have a child in another section, otherwise select "Not Applicable".')

    photo_permission = forms.ChoiceField(
        choices = (
            ('Yes', 'Yes'),
            ('No', 'No')
        ),
        label='Photographic Permission', widget=forms.RadioSelect(),
        help_text='Please let us know whether we have your permission to share your childs photos on this website.')

    theme = forms.ChoiceField(
        choices = (
            ('Dark', 'Dark Theme'),
            ('Light', 'Light Theme')
        ),
        label='Colour Theme', widget=forms.RadioSelect(),
        help_text='Please select your colour theme.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('username', 'Username*'),
            PrependedText('email', 'Email*'),
            'section',
            'second_section',
            'photo_permission',
            'theme',
            HTML('<button class="btn btn-outline-info" type="submit">'
                '<i class="fa-duotone fa-circle-check"></i> Submit'
                '</button>')
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'section', 'second_section', 'photo_permission', 'theme']

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