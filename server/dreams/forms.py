from django import forms
from .models import Dream
import os

class DreamForm(forms.ModelForm):
    extra_field = forms.CharField(required=False, label="Extra Info")

    class Meta:
        model = Dream
        fields = ['name']
        labels = {
            'name': 'Giev this dream a unique name!',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ex: Super Crazy Dream'}),
        }
