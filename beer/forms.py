from django import forms
from .models import Beer

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('beer_name', 'brewery', 'abv')