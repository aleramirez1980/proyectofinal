from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ModificacionUsuarioForm
from django.contrib.auth.views import PasswordChangeView




def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario registrado ¡Bienvenido!')
            return redirect('RegistroExitoso')
        
        
    else:
        messages.error(request, 'El usuario no pudo ser creado por no cumplir la validación')
        form = RegistroUsuarioForm()
        
        
    return render(request, 'registro/registro.html', {'form': form })



class RegistroExitoso(TemplateView):
    
    template_name = 'registro/pantalla_registro.html'


class ModificarUsuario(UpdateView):
    model = User
    form_class = ModificacionUsuarioForm
    template_name = 'registro/editar_usuario.html'
    success_url = reverse_lazy('EdicionExitosa') 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El usuario ha sido modificado exitosamente.')
        return response
 
    def get_object(self, queryset=None):
        return self.request.user
    
    
class EdicionExitosa(TemplateView):
    
    template_name = 'registro/pantalla_edicion.html'
    
    


class CambioContrasena(PasswordChangeView):
    template_name = 'registro/cambio_contrasena.html'
    success_url = reverse_lazy('CambioContrasenaExitoso')
    
    
    
    
class CambioClave(TemplateView):
    
    template_name = 'registro/pantalla_clave.html'
    
    