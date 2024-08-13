from django.db import models

# Create your models here.
class Electrica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    imagen = models.ImageField(upload_to='media/') # Se agrega campo de imagenes. 
    
    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.anio}'
    
    
class Acustica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.anio}'

class Amplificador(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.IntegerField(null=True)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True) 
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.anio}'
    
class Efecto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)   
    imagen = models.ImageField(upload_to='media/')
    
def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.anio}'