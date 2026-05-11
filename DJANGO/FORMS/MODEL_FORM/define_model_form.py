# We can make a form to save data for specific form its model form 

from django import forms
from .models import Model_I_Want
class ModelForm(forms.ModelForm):
    class Meta:
        model = Model_I_Want
        fields = ['title', 'content']
        