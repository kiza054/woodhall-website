import os

from django import forms
from django_summernote.widgets import SummernoteWidget
from taggit_labels.widgets import LabelWidget

from accounts.models import User
from cubs.models import Comment, File, Post, PostImage


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    author = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    #image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'status')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

class UploadFileForm(forms.ModelForm):
    name = forms.CharField(help_text='Name of file to be uploaded (e.g. camp_form.docx)')
    description = forms.CharField(help_text='What is the file used for, add some explanation.')
    class Meta:
        model = File
        fields = ('name', 'description', 'file')