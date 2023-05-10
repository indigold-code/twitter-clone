from django import forms 
from .models import Chirp


class ChirpForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter Your Cloner Chirp!",
                "class":"form-control",
            }
            ),
            label="",           
            )
    class Meta:
        model = Chirp
        exclude = ("user",)