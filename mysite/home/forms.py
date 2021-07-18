from django import forms
from django.core import validators
from home.models import Musician,Album

class Musician_form(forms.ModelForm): # creating forms using model objects
    class Meta:
        model = Musician #model name
        fields = "__all__" #selected fields
