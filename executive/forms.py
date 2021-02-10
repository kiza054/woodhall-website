from django import forms
from executive.models import QuartermastersItemInventory

class QuartermastersItemInventoryForm(forms.ModelForm):
    class Meta:
        model = QuartermastersItemInventory
        fields = ['item_name', 'category', 'notes']