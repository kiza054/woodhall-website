from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit
from django import forms
from django_summernote.widgets import SummernoteWidget
from taggit_labels.widgets import LabelWidget

from accounts.models import User
from scouts.models import Comment, File, Post, PostImage


class PostForm(forms.ModelForm):
    title = forms.CharField(label='')
    author = forms.ModelChoiceField(label='', queryset=User.objects.filter(is_staff=True))
    content = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    #image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
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
            PrependedText('title', 'Title:'),
            PrependedText('author', 'Author:'),
            'content',
            'status',
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-mailbox"></i> Post'
                    '</button>')
                )
            )

    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'status')

class CommentForm(forms.ModelForm):
    name = forms.CharField(label='')
    email = forms.CharField(label='')
    comment = forms.CharField(label='')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('name', 'Name:'),
            PrependedText('email', 'Email:'),
            PrependedText('comment', 'Comment:'),
            FormActions(
                HTML('<button type="submit" class="btn btn-outline-info btn-me">'
                    '<i class="fa-duotone fa-circle-check"></i> Submit'
                    '</button>')
                )
            )

    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

class UploadFileForm(forms.ModelForm):
    name = forms.CharField(label='', help_text='Name of file to be uploaded (e.g. camp_form.docx)')
    description = forms.CharField(label='', help_text='What is the file used for, add some explanation.')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('name', 'Name:'),
            PrependedText('description', 'Description:'),
            'file',
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-upload"></i> Upload'
                    '</button>')
                )
            )
    
    class Meta:
        model = File
        fields = ('name', 'description', 'file')