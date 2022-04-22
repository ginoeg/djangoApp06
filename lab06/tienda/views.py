from django.shortcuts import get_object_or_404, render

from .models import Categoria, Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    return render(request, 'producto.html', {'producto': producto , 'categorias': categorias})


def mostrar(request, categoria_id):
    lista_producto = get_object_or_404(Categoria, pk=categoria_id)
    context = {'lista_producto': lista_producto}
    return render(request, 'mostrar.html', context)