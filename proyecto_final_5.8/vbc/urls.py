from django.urls import path
from vbc import views

urlpatterns = [
    path("electricas/lista", views.ElectricaListView.as_view(), name = "ListaElectricas"),
    path("electricas/nuevo", views.ElectricaCreateView.as_view(), name = "NuevaElectrica"),
    path("electricas/<pk>", views.ElectricaDetailView.as_view(), name = "DetalleElectrica"),
    path("electricas/<pk>/editar", views.ElectricaUpdateView.as_view(), name = "EditarElectrica"),
    path("electricas/<pk>/borrar", views.ElectricaDeleteView.as_view(), name = "BorrarElectrica"),
    
    path("acusticas/lista", views.AcusticaListView.as_view(), name = "ListaAcusticas"),
    path("acusticas/nuevo", views.AcusticaCreateView.as_view(), name = "NuevaAcustica"),
    path("acusticas/<pk>", views.AcusticaDetailView.as_view(), name = "DetalleAcustica"),
    path("acusticas/<pk>/editar", views.AcusticaUpdateView.as_view(), name = "EditarAcustica"),
    path("acusticas/<pk>/borrar", views.AcusticaDeleteView.as_view(), name = "BorrarAcustica"),

    path("amplificadores/lista", views.AmplificadorListView.as_view(), name = "ListaAmplificadores"),
    path("amplificadores/nuevo", views.AmplificadorCreateView.as_view(), name = "NuevoAmplificador"),
    path("amplificadores/<pk>", views.AmplificadorDetailView.as_view(), name = "DetalleAmplificador"),
    path("amplificadores/<pk>/editar", views.AmplificadorUpdateView.as_view(), name = "EditarAmplificador"),
    path("amplificadores/<pk>/borrar", views.AmplificadorDeleteView.as_view(), name = "BorrarAmplificador"),  

    path("efectos/lista", views.EfectoListView.as_view(), name = "ListaEfectos"),
    path("efectos/nuevo", views.EfectoCreateView.as_view(), name = "NuevoEfecto"),
    path("efectos/<pk>", views.EfectoDetailView.as_view(), name = "DetalleEfecto"),
    path("efectos/<pk>/editar", views.EfectoUpdateView.as_view(), name = "EditarEfecto"),
    path("efectos/<pk>/borrar", views.EfectoDeleteView.as_view(), name = "BorrarEfecto"),   
]