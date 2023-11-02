from django.shortcuts import render
from .models import Producto, Pedido

def index(request):
    return render(request, 'mi_app/index.html')

def lista_productos(request):
    productos = Producto.objects.all()  # Recupera todos los productos desde la base de datos
    return render(request, 'mi_app/lista_productos.html', {'productos': productos})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()  # Recupera todos los pedidos desde la base de datos
    return render(request, 'mi_app/lista_pedidos.html', {'pedidos': pedidos})
