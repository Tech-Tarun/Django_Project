from django import forms
from .models import Details

class SaveDetails(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['user','email','pas','passcon','add','add1','city','state','zip']