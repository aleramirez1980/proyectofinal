from django import forms
    
class BuscaElectricaForm(forms.Form):
    marca=forms.CharField(max_length=50)
    
class BuscaAcusticaForm(forms.Form):
    marca=forms.CharField(max_length=50)    
    
class BuscaAmplificadorForm(forms.Form):
    marca=forms.CharField(max_length=50)
    
class BuscaEfectoForm(forms.Form):
    marca=forms.CharField(max_length=50)