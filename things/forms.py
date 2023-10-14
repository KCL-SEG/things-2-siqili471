"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    widgets = {
        'description': forms.Textarea(attrs={'row':4,'cols':50}),
        'quantity':forms.NumberInput(attrs={'min':0}),
    }