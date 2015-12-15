from django.conf.urls import patterns, include, url
from .views import index

urlpatterns = patterns('',
    url(r'^$' , 'inicio.views.index'), #dar la vista que creamos
    url(r'^oferta/' , 'inicio.views.oferta'),
    url(r'^galeria/' , 'inicio.views.galeria'),
    url(r'^contacto/' , 'inicio.views.contacto'),

)
