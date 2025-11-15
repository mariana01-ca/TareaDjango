from django.contrib import admin
from django.urls import path, include
from appVentas import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('index', views.index, name='index'),
    path('clientes/', views.listar_clientes, name = "listar_clientes"),
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('nuevo_cliente/', views.crear_cliente, name= "crear_cliente"),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente, name ="eliminar_cliente"),
    path('actualizar_cliente/<int:id>', views.artualizar_cliente, name="actualizar_cliente"),
    path('nueva_tienda/', views.crear_tienda, name= "crear_tienda"),
    path('eliminar_tienda/<int:id>', views.eliminar_tienda, name ="eliminar_tienda"),
    path('actualizar_tienda/<int:id>', views.artualizar_tienda, name="actualizar_tienda"),
    path('compras/', views.listar_compras, name="listar_compras"),
    path('compras/nueva/', views.crear_compra, name="crear_compra"),
    path('compras/eliminar/<int:id>/', views.eliminar_compra, name="eliminar_compra"),
    path('compras/actualizar/<int:id>/', views.actualizar_compra, name="actualizar_compra"),
    path('logout/',views.cerrar_sesion,name="logout"),
]