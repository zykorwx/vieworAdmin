from django.db import models
from django.contrib.auth.models import User
# Esta linea deber modificada segun la tabla donde se vaya agregar comentarios
# se pueden agregar cuantas tablas sean nesesarias
from principal.models import Noticia

# Create your models here.
# Recordar que django agrega automaticamente a los nombres de las tablas
# en la base de datos un prefijo por ejemplo el nombre del modelo Comentario
# en la base de datos seria comentarios_comentario
# por lo cual se puede permitir repetir los nombres

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(help_text='Escribe tu comentario aqui')
    fecha_publicacion = models.DateTimeField(auto_now=True)

def __unicode__(self):
        return self.titulo

# Se agregan los modelos de las tablas
# Primero la estructura del nombre tabla_comentarios
# La estructura lleva el la fk del objeto que tendra los comentarios
# llevara el id del comentario

class Noticia_comentarios(models.Model):
    id_noticia = models.ForeignKey(Noticia)
    id_comentario = models.ForeignKey(Comentario)
