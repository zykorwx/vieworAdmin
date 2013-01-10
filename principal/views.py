#encoding:utf-8
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from principal.models import Noticia, Tarea, Asigna_tarea
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.




def ingresar(request):
    if request.method == 'POST':
        formulario_login = AuthenticationForm(request.POST)
        if formulario_login.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                login(request, acceso)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('Mensajes/noactivo.html', context_instance=RequestContext(request))
        else:
            return render_to_response('Mensajes/noactivo.html', context_instance=RequestContext(request))
    else:
        formulario_login = AuthenticationForm()
    return render_to_response('formularios/Ingresar.html', {'formulario_login':formulario_login}, context_instance=RequestContext(request))


@login_required(login_url='/inresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def mostrar_noticias(request):
    noticias = Noticia.objects.filter(estado=True)
    return render_to_response('base/base_noticias.html',{'noticias': noticias}, context_instance=RequestContext(request))

def mostrar_noticia(request, id_noticia):
    dato = get_object_or_404(Noticia, pk=id_noticia)
    return render_to_response('base/base_noticia.html',{'dato': dato}, context_instance=RequestContext(request))
