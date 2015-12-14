from django.conf.urls import patterns, include, url
from .views import index

urlpatterns = patterns(
    url(r'^$' , 'escuela.views.index'),
)
