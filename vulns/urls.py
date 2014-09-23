from django.conf.urls import patterns, url

from vulns import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^test/$', views.index, name='index'),
    url(r'^problematica/$', views.problematica, name='problematica'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^(?P<ip>(\d{1,3})\.\d{1,3}\.\d{1,3}\.\d{1,3})/$', views.test, name='test'),
)