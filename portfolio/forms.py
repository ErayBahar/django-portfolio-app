from django import forms
from .models import portfolioItem

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = portfolioItem
        fields = ["symbol","boughtPrice","amount"]