# -*- coding: utf-8 *-*
from principal.models import Noticia, Tarea, Asigna_tarea
from comentarios.models import Noticia_comentarios, Comentario
from django.contrib import admin

admin.site.register(Tarea)
admin.site.register(Noticia)
admin.site.register(Asigna_tarea)
admin.site.register(Noticia_comentarios)
admin.site.register(Comentario)

