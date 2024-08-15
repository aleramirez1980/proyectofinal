from django.db import models

# Create your models here.
class Electrica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    email_contacto = models.EmailField(max_length=50, null=True) 

class Acustica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    email_contacto = models.EmailField(max_length=50, null=True)

class Amplificador(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.IntegerField(null=True)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    email_contacto = models.EmailField(max_length=50, null=True) 
    
class Efecto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    email_contacto = models.EmailField(max_length=50, null=True)   