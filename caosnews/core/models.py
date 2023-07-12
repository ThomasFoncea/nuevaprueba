from django.db import models

# Create your models here.

#Modelo para la Categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCatgoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    def __str__(self):
        return self.nombreCatgoria

#Modelo para el Vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=15, primary_key=True, verbose_name='Nombre del Periodista')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, verbose_name='Tipo de Noticia')
    modelo = models.CharField(max_length=10, null=True, verbose_name='Fecha publicación')
    marca = models.CharField(max_length=15, verbose_name='Titulo')
    cuerpo = models.CharField(max_length=150, verbose_name='Cuerpo')
    imagen = models.ImageField(upload_to='static/img', null=True, blank=True, verbose_name='Imagen')


    def __str__(self):
        return self.patente

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()