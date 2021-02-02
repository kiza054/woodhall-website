from django import forms
from taggit.forms import TagField
from django.forms import DateInput
from taggit_labels.widgets import LabelWidget
from main_website.models import Article, WaitingList, Event, ImageGallery

class ArticleForm(forms.ModelForm):
    tags = TagField(required=False, widget=LabelWidget)
    class Meta:
        model = Article
        fields = ('article_name', 'author', 'content', 'tags', 'status')

class WaitingListForm(forms.ModelForm):
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
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('file_name', 'image')