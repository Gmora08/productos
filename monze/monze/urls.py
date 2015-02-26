from django.conf.urls import patterns, include, url
from django.contrib import admin
from producto import views as vproductos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',vproductos.index, name = 'inicio'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^conocenos/$', vproductos.conocenos, name='conocenos'),
    url(r'^politicas/$', vproductos.politicas, name='politicas'),
    url(r'^contacto/$', vproductos.contacto, name='contacto'),    
    url(r'^producto/$', vproductos.productos, name='productos'),
    url(r'^producto/agregar/$', vproductos.AgregarProducto.as_view(), name="agregar-producto"),
    url(r'^producto/editar/(?P<id_producto>\d{1,})/$', vproductos.EditarProducto.as_view(), name="editar-producto"),
    url(r'^producto/eliminar/(?P<id_producto>\d{1,})/$', vproductos.eliminarProducto, name="borrar-producto"),

)
