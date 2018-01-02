from django.forms import ModelForm
from .models import Property
from django import forms

class AddProperty(ModelForm):
    date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
    class Meta:
        model = Property
        exclude=['price_per_ft2',]