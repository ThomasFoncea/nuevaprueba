from django.db import models
class contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    direccion = models.CharField(max_length=50, verbose_name='direccion')
    telefono = models.IntegerField(primary_key=True, verbose_name='telefono')
    correo = models.CharField(max_length=50, verbose_name='correo')
    mensaje = models.CharField(max_length=200, verbose_name='mensaje')
    def __str__(self):
        return self.nombre
# Create your models here.
