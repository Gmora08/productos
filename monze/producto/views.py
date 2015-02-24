from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from .forms import ProductoForm
from .models import Producto

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

class AgregarProducto(View):
    def get(self, request):     
        form = ProductoForm()
        return render(request, 'agregar-producto.html', {'form': form})
    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u"Producto %s creado con exito " % request.POST['nombre'])

        else:
            messages.error(request, u"ingresa mal algunos datos")
            return render(request, 'agregar-producto.html', {'form':form})

