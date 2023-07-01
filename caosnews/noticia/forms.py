from django import forms
from django.forms import ModelForm
from.models import contacto
# Create your forms here.
# class ContactoForm(ModelForm):
#     class Meta:
#         model = contacto
#         fields = ['nombre','correo','telefono','direccion','mensaje']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre', 'direccion', 'telefono', 'correo', 'mensaje']
        labels = {
            'nombre': 'Nombre del Periodista',
            'direccion': 'Tipo de Noticia',
            'telefono': 'Fecha Publicacion',
            'correo': 'Titulo',
            'mensaje': 'Cuerpo',
        }