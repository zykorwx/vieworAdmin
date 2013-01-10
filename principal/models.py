#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Noticia(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    contenido = models.TextField(help_text='Escribe el contenido de la noticia aqui')
    fecha_publicacion = models.DateTimeField(auto_now=True)
    imagen_entrada = models.ImageField(upload_to='noticias', verbose_name='Imagen')
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo


class Tarea(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(help_text='Descripcion de la tarea a realizar')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_limite = models.DateTimeField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre


class Asigna_tarea(models.Model):
    usuario_asignado = models.ForeignKey(User)
    tarea_asignada = models.ForeignKey(Tarea)




