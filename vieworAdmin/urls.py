from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
#Urls personales
    url(r'^$', 'principal.views.inicio'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
#Urls para activar el administrador de python
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
#Url creada para decirle al sistema donde buscar los archivos subidos
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, }
    ),
)
