from django.conf.urls import patterns, include, url
from django.contrib import admin
from producto import views as vproductos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^producto', vproductos.productos, name="mostrar"),
    url(r'^producto/agregar', vproductos.AgregarProducto.as_view(), name="agregar-producto"),
)
