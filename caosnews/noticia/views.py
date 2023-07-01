from django.shortcuts import  render, redirect  
from django.contrib.auth import login 
from django.contrib import messages
from .forms import ContactoForm
from .models import contacto

#from .models import
#from .forms import 
#Create your views here.
def paginaprincipal(request):
    return render(request,'paginaprincipal.html')

def deporte(request):
    return render(request,'deporte.html')

def policial(request):
    return render(request,'policial.html')

def tendencia(request):
    return render(request,'tendencia.html')

def nacional(request):
    return render(request,'nacional.html')

def login(request):
    return render(request,'login.html')

def contacto_view(request):
    contactos = contacto.objects.all()
    return render(request, 'contacto.html', {'contactos': contactos}) 

def eliminar_contacto(request, nombre):
    contactos = contacto.objects.get(nombre=nombre)
    contactos.delete()
    return redirect('contacto')

def recuperarcontraseña(request):
    return render(request,'recuperarcontraseña.html')

def form_contacto(request):
    datos = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente" 
            redirect('contacto')
    return render(request, 'form_contacto.html', datos)

def form_mod_contacto(request, tel):
    contacto = contacto.objects.get(telefono=tel)
    datos = {
        'form': ContactoForm(instance=contacto)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance=contacto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
    return render(request, 'form_mod_contacto.html', datos)