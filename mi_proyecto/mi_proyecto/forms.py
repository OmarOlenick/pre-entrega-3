from django import forms
from .models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'  
