from django import forms
from core.models import Log

class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ['subject']