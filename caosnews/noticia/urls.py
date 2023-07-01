"""caosnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('paginaprincipal/',views.paginaprincipal,name='paginaprincipal'),

    path('deporte/',views.deporte,name='deporte'),

    path('policial/',views.policial,name='policial'),

    path('tendencia/',views.tendencia,name='tendencia'),

    path('nacional/',views.nacional,name='nacional'),

    path('contacto/',views.contacto_view,name='contacto'),
    
    path('login/',views.login,name='login'),  

    path('recuperarcontraseña/',views.recuperarcontraseña,name='recuperarcontraseña'),

    path('form_contacto/',views.form_contacto,name='form_contacto'),

    path('form-mod-contacto/<tel>',views.form_mod_contacto, name="form_mod_contacto"),

    path('contacto/eliminar/<str:nombre>/', views.eliminar_contacto, name='eliminar_contacto'),



]