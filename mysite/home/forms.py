from django import forms
from django.core import validators
from home import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"
        include = ['release_date']
