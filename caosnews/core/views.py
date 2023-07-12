from django.shortcuts import render, redirect
from .models import Vehiculo, Categoria, Contacto
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

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


def mod_crud(request):
     vVehiculos = Vehiculo.objects.all()
     datos = {'vehiculos':vVehiculos}
     return render(request, 'mod_crud.html', datos)

def form_perrito(request):
    datos ={
        'form':VehiculoForm()
        }
    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados correctamente"
    return render(request, 'form_perrito.html',datos)


def crud(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'vehiculos':vVehiculos}
    return render(request, 'crud.html', contexto)


@staff_member_required
def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            vehiculo.delete()
            vehiculos = Vehiculo.objects.all()  # Recupera la lista de vehículos actualizada
            datos['vehiculos'] = vehiculos
            datos['mensaje'] = "Registro eliminado correctamente"
            return render(request, 'mod_crud.html', datos)  # Redirige a la misma página actualizada
        else:
            formulario = VehiculoForm(data=request.POST, instance=vehiculo)
            if formulario.is_valid:
                formulario.save()
                datos['mensaje'] = "Registro actualizado correctamente"
    return render(request, 'form_mod_vehiculo.html', datos)



def gatos(request):
    return render(request, 'gatos.html')


def index(request):
    return render(request, 'index.html')


def perros(request):
    return render(request, 'perros.html')


def form_contacto(request):
    return render(request, 'form-contacto.html')


@login_required
def sesion(request):
    return render(request,'paginaprincipal.html')

def salir(request):
    logout(request)
    return redirect('/')


def crearcuenta(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect(to='paginaprincipal')
        else:
            # Agrega tu lógica de validación adicional para la contraseña aquí
            password1 = form.cleaned_data.get('password1')
            if len(password1) < 8:
                messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            if not any(char.isdigit() for char in password1):
                messages.error(request, "La contraseña debe contener al menos un número.")
            # Agrega más validaciones según tus requisitos

            # Renderiza nuevamente el formulario con los errores
            return render(request=request, template_name="crearcuenta.html", context={"register_form": form})
    else:
        form = NewUserForm()
    return render(request=request, template_name="crearcuenta.html", context={"register_form": form})

def respuesta(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']
        
        # Guardar los datos en la base de datos
        contacto = Contacto(nombre=nombre, correo=correo, mensaje=mensaje)
        contacto.save()
        
        return redirect('respuesta')
    
    return render(request, 'respuesta.html')
