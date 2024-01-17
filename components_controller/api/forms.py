# games/forms.py
from django import forms


class GameSearchForm(forms.Form):
    """
    Această clasă definesc un formular simplu pentru căutarea jocurilor.
    """
    query = forms.CharField(label='Search', max_length=100)
