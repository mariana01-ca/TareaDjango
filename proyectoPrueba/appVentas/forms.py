from django import forms 
from .models import Cliente
from .models import Tienda

class clienteForm(forms.Form):
    nombre = forms.CharField(label = "Nombre",required=True)
    correo = forms.CharField(label = "Correo", required=True)
    
class tiendaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", required=True)
    direccion = forms.CharField(label = "Direccion", required=True)    

class compraForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    monto = forms.DecimalField(max_digits=10, decimal_places=2)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    tienda = forms.ModelChoiceField(queryset=Tienda.objects.all())
    