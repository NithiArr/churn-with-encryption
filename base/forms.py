from django import forms
from base.models import customer

class stform(forms.ModelForm):
    class Meta:
        model = customer
        fields="__all__"