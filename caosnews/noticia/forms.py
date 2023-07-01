from django import forms
from django.forms import ModelForm
from.models import contacto
# Create your forms here.
class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre','correo','telefono','direccion','mensaje']