from django.db import models
from django import forms

# Create your models here.
class Dream(models.Model):
    name = models.CharField(max_length=100)

class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['name']
