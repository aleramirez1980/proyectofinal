from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Electrica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_hora= models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    imagen = models.ImageField(upload_to='media/') # Se agrega campo de imagenes. 
    
  
       
    
    def __str__(self):
        fecha_format = self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        return f'{self.marca}, {self.modelo}, {self.anio}, creado el  {fecha_format}'
    
    
class Acustica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_hora= models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        fecha_format = self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        return f'{self.marca}, {self.modelo}, {self.anio}, creado el  {fecha_format}'

class Amplificador(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.IntegerField(null=True)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True) 
    fecha_hora= models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        fecha_format = self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        return f'{self.marca}, {self.modelo}, {self.anio}, creado el  {fecha_format}'
    
class Efecto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.IntegerField(null=True)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True)  
    fecha_hora= models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
       fecha_format = self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
       return f'{self.marca}, {self.modelo}, {self.anio}, creado el  {fecha_format}'