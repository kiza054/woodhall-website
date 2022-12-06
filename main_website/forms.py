from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit
from django import forms
from django.forms import DateInput
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget

from accounts.models import User
from main_website.models import (Article, Event, ImageGallery,
                                 ImageGalleryCategory, WaitingList)


class ArticleForm(forms.ModelForm):
    article_name = forms.CharField()
    author = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    content = forms.CharField(
        max_length=2000, 
        widget=forms.TextInput(attrs={'cols': 80, 'rows': 20})
    )
    tags = TagField(required=False, widget=LabelWidget)
    status = forms.ChoiceField(
        choices = (
            ('Draft', 'Draft'),
            ('Published', 'Published')
        ),
        widget=forms.RadioSelect()
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('article_name', 'Title:'),
            PrependedText('author', 'Author:'),
            'content',
            'tags',
            'status',
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-mailbox"></i> Post'
                    '</button>')
                )
            )
    class Meta:
        model = Article
        fields = ('article_name', 'author', 'content', 'tags', 'status')

class WaitingListForm(forms.ModelForm):
    first_name = forms.CharField(label='')
    last_name = forms.CharField(label='')
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=''
    )
    section_of_interest = forms.ChoiceField(
        choices = (
            ('Beavers', 'Beavers'),
            ('Cubs', 'Cubs'),
            ('Scouts', 'Scouts'),
            ('Unsure of Section', 'Unsure of Section')
        ),
        widget=forms.RadioSelect()
    )
    name_of_parent_carer = forms.CharField(label='Name of Parent/Carer')
    parent_carer_email = forms.EmailField(label='Email of Parent/Carer')
    parent_carer_phone_number = forms.CharField(label='Phone Number of Parent/Carer')
    parent_carer_address = forms.CharField(label='Address of Parent/Carer')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('first_name', 'First Name:'),
            PrependedText('last_name', 'Last Name:'),
            PrependedText('date_of_birth', 'DoB:'),
            'section_of_interest',
            PrependedText('name_of_parent_carer', 'Full Name:'),
            PrependedText('parent_carer_email', 'Email:'),
            PrependedText('parent_carer_phone_number', 'Phone:'),
            PrependedText('parent_carer_address', 'Address:'),
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-circle-check"></i> Submit'
                    '</button>')
                )
            )

    class Meta:
        model = WaitingList
        fields = (
            'first_name', 
            'last_name', 
            'date_of_birth', 
            'section_of_interest', 
            'name_of_parent_carer',
            'parent_carer_email',
            'parent_carer_phone_number',
            'parent_carer_address'
        )

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['subject'].label = "Subject:"
        self.fields['content'].label = "Your Query:"

class EventForm(forms.ModelForm):
    title = forms.CharField(label='', help_text='Name of the event.')
    description = forms.CharField(label='', widget=forms.Textarea, help_text='Description of event, describe whats happening at the event.')
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['start_time'].label = ''
        self.fields['start_time'].help_text = "Time the event starts."
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].label = ''
        self.fields['end_time'].help_text = "Time the event ends."

        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('title', 'Title:'),
            PrependedText('description', 'Description:'),
            PrependedText('start_time', 'Start Time:'),
            PrependedText('end_time', 'End Time:'),
            FormActions(
                HTML('<button type="submit" class="btn btn-custom-purple">'
                    '<i class="fa-duotone fa-calendar-plus"></i> Submit'
                    '</button>')
                )
            )

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('category', 'file_name', 'image', 'description')
        
    def __init__(self, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = 4
        self.fields['description'].widget.attrs['cols'] = 40
        self.fields['description'].widget.attrs['columns'] = 15

class AddImageCategoryForm(forms.ModelForm):
    class Meta:
        model = ImageGalleryCategory
        fields = ('user', 'name')