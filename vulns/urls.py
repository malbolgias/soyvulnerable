from django.conf.urls import patterns, url

from vulns import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^test/$', views.index, name='index'),
    url(r'^problematica/$', views.problematica, name='problematica'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^guion/$', views.guion, name='guion'),
    url(r'^solucion/$', views.guion, name='solucion'),
)