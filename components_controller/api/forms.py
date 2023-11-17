# games/forms.py
from django import forms


class GameSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
