from django import forms
from .models import Signup

class Form1(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'




