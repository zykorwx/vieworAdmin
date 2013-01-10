#encoding:utf-8
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from comentarios.models import Noticia_comentarios
from principal.models import Noticia
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def mostrar_noticia_comentarios(request):
    comentarios = Noticia_comentarios.objects.get(id_noticia=request.Noticia.pk)
    return render_to_response('base/base_noticias.html',{'comentarios': comentarios}, context_instance=RequestContext(request))
