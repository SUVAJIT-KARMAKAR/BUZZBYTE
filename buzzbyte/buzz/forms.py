# BUZZ -> FORMS -> FORMS.PY
from django import forms
from .models import Buzz

class BuzzForm(forms.ModelForm):
    class Meta :
        model = Buzz
        fields = ['text', 'photo']
