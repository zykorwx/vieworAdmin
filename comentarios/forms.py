# -*- coding: utf-8 *-*
from django.forms import ModelForm
from django import forms
from comentarios.models import Comentario

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ('titulo', 'contenido')
