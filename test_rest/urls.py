from django.conf.urls import url
from apprest import views

urlpatterns = [
    url(r'^libro/$', views.lista_libro),
    url(r'^autor/$', views.lista_autor),
    url(r'^/$', views.index),
]
