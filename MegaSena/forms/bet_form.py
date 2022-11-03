from django import forms
from django.contrib.auth.models import User

from MegaSena.models import Bet


class BetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Bet
        fields = '__all__'
