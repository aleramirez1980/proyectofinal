from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    
    path("registrar_usuario/", views.registro , name="Registro"),
    path("registro_exitoso/", views.RegistroExitoso.as_view() , name="RegistroExitoso"),
    path('editar_usuario/', views.ModificarUsuario.as_view(), name='EditarUsuario'),
    path("edicion_exitosa/", views.EdicionExitosa.as_view() , name="EdicionExitosa")
    
]
