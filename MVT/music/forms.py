from django import forms
##from datetime import datetime


class ArtistaFormulario(forms.Form):
    alias = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class AlbumFormulario(forms.Form):
    nombre = forms.CharField()
    fechaDePublicacion = forms.DateField()
    artista = forms.CharField()

class CancionFormulario(forms.Form):
    nombre = forms.CharField()
    album = forms.CharField()