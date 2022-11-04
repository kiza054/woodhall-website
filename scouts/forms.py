import os

from django import forms
from django.core.mail import EmailMultiAlternatives, send_mail
from django_summernote.widgets import SummernoteWidget
from taggit_labels.widgets import LabelWidget

from accounts.models import User
from scouts.models import Comment, File, Post, PostImage


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    author = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    #image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'status')

    """
    def send_email(self):
        sender = os.environ.get('EMAIL_USER')
        subject = '1st Woodhall Cubs Blog | New Blog Post'
        text_content = 'Hello there, there has been a new post published on the blog'
        html_content = '<p>Hello there, there has been a new post published on the blog</p>'
        recipients = []
        for users in User.objects.all():
            recipients.append(users.email)
        msg = EmailMultiAlternatives(subject, text_content, sender, recipients)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
    """

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'description', 'file')