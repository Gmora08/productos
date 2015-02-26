from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.contrib import messages
from .forms import ProductoForm
from .models import Producto

def index(request):
    return render(request,'index.html', {})

def productos(request):
    print "hola"
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

class EditarProducto(View):
    def get(self, request, id_producto):
        print "ya entre"
        buscar = get_object_or_404(Producto, pk=id_producto)
        form = ProductoForm(instance=buscar)
        return render(request, 'editar-producto.html', {'form': form})

    def post(self, request, id_producto):
        buscar = get_object_or_404(Producto, pk=id_producto)
        form = ProductoForm(request.POST, instance=buscar)
        if form.is_valid():
            form.save()
            messages.success(request, u"Producto %s editado con exito " % request.POST['nombre'])
            return redirect(reverse('productos'))
        else:
            messages.error(request, u"ingresa mal algunos datos")
            return render(request, 'editar-producto.html', {'form':form})


class AgregarProducto(View):
    def get(self, request):     
        form = ProductoForm()
        return render(request, 'agregar-producto.html', {'form': form})
    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u"Producto %s creado con exito " % request.POST['nombre'])
            return redirect(reverse('productos'))
            

        else:
            messages.error(request, u"ingresa mal algunos datos")
            return render(request, 'agregar-producto.html', {'form':form})

def eliminarProducto(request, id_producto):
        buscar = get_object_or_404(Producto, pk=id_producto)
        buscar.delete()
        return redirect(reverse('productos'))