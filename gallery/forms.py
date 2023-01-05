from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout
from django import forms

from accounts.models import User
from gallery.models import (ImageGallery, ImageGalleryCategory)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('category', 'file_name', 'image', 'description')
    
    def __init__(self, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('category', 'Category:'),
            PrependedText('file_name', 'File Name:'),
            'image',
            PrependedText('description', 'Description:'),
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-file-arrow-up"></i> Upload Images'
                    '</button>')
                )
            )
        self.fields['description'].widget.attrs['rows'] = 4
        self.fields['description'].widget.attrs['cols'] = 40
        self.fields['description'].widget.attrs['columns'] = 15
        self.fields['category'].label = ''
        self.fields['file_name'].label = ''
        self.fields['image'].label = ''
        self.fields['description'].label = ''

class AddImageCategoryForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))

    def __init__(self, *args, **kwargs):
        super(AddImageCategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            PrependedText('user', 'User:'),
            PrependedText('name', 'Name:'),
            FormActions(
                HTML('<button class="btn btn-outline-info" type="submit">'
                    '<i class="fa-duotone fa-plus"></i> Add Category'
                    '</button>')
                )
            )
        self.fields['user'].label = ''
        self.fields['name'].label = ''

    class Meta:
        model = ImageGalleryCategory
        fields = ('user', 'name')