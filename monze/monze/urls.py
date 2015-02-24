from django.conf.urls import patterns, include, url
from django.contrib import admin
from producto import views as vproductos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^producto/$', vproductos.productos, name='productos'),
    url(r'^producto/agregar/$', vproductos.AgregarProducto.as_view(), name="agregar-producto"),
    url(r'^producto/editar/(?P<id_producto>\d{1,})/$', vproductos.EditarProducto.as_view(), name="editar-producto"),

)
