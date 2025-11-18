from django import forms 
from . import models #this imports models.py in the current folder

class CreateCard(forms.ModelForm):
    class Meta:
        model = models.Cards
        fields = ['title','body','slug','banner']