from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from app.models import Electrica
from app.models import Acustica
from app.models import Amplificador
from app.models import Efecto

class ElectricaListView(ListView):
    model = Electrica
    context_object_name = "Electricas"
    template_name = "vbc/lista_electricas.html"
    
class ElectricaDetailView(DetailView):
    model = Electrica
    template_name = "vbc/electricas_detalle.html"
    
class ElectricaCreateView(CreateView):
    model = Electrica
    template_name = "vbc/electricas_crear.html"
    success_url = reverse_lazy("ListaElectricas")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"]
    
class ElectricaUpdateView(UpdateView):
    model = Electrica
    template_name = "vbc/electricas_editar.html"
    success_url = reverse_lazy("ListaElectricas")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"] 
    
class ElectricaDeleteView(DeleteView):
    model = Electrica
    template_name = "vbc/electricas_borrar.html"
    success_url = reverse_lazy("ListaElectricas")

class AcusticaListView(ListView):
    model = Acustica
    context_object_name = "Acusticas"
    template_name = "vbc/lista_acusticas.html"
    
class AcusticaDetailView(DetailView):
    model = Acustica
    template_name = "vbc/acusticas_detalle.html"
    
class AcusticaCreateView(CreateView):
    model = Acustica
    template_name = "vbc/acusticas_crear.html"
    success_url = reverse_lazy("ListaAcusticas")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"]
    
class AcusticaUpdateView(UpdateView):
    model = Acustica
    template_name = "vbc/acusticas_editar.html"
    success_url = reverse_lazy("ListaAcusticas")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"] 
    
class AcusticaDeleteView(DeleteView):
    model = Acustica
    template_name = "vbc/acusticas_borrar.html"
    success_url = reverse_lazy("ListaAcusticas")

class AmplificadorListView(ListView):
    model = Amplificador
    context_object_name = "Amplificadores"
    template_name = "vbc/lista_amplificadores.html"
    
class AmplificadorDetailView(DetailView):
    model = Amplificador
    template_name = "vbc/amplificadores_detalle.html"
    
class AmplificadorCreateView(CreateView):
    model = Amplificador
    template_name = "vbc/amplificadores_crear.html"
    success_url = reverse_lazy("ListaAmplificadores")
    fields = ["marca", "modelo", "potencia", "serial", "anio", "precio", "descripcion"]
    
class AmplificadorUpdateView(UpdateView):
    model = Amplificador
    template_name = "vbc/amplificadores_editar.html"
    success_url = reverse_lazy("ListaAmplificadores")
    fields = ["marca", "modelo", "potencia", "serial", "anio", "precio", "descripcion"] 
    
class AmplificadorDeleteView(DeleteView):
    model = Amplificador
    template_name = "vbc/amplificadores_borrar.html"
    success_url = reverse_lazy("ListaAmplificadores")

class EfectoListView(ListView):
    model = Efecto
    context_object_name = "Efectos"
    template_name = "vbc/lista_efectos.html"
    
class EfectoDetailView(DetailView):
    model = Efecto
    template_name = "vbc/efectos_detalle.html"
    
class EfectoCreateView(CreateView):
    model = Efecto
    template_name = "vbc/efectos_crear.html"
    success_url = reverse_lazy("ListaEfectos")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"]
    
class EfectoUpdateView(UpdateView):
    model = Efecto
    template_name = "vbc/efectos_editar.html"
    success_url = reverse_lazy("ListaEfectos")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"] 
    
class EfectoDeleteView(DeleteView):
    model = Efecto
    template_name = "vbc/efectos_borrar.html"
    success_url = reverse_lazy("ListaEfectos")