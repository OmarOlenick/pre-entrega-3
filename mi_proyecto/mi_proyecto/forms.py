from django import forms
from .models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario
