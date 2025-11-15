from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Tienda
from .models import Compra
from .forms import clienteForm
from .forms import tiendaForm
from .forms import compraForm
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar_clientes(request):
    clientes = Cliente.objects.all() #decir selct* from clientes
    return render (request,'listar_clientes.html', {'clientes':clientes})

def listar_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'listar_tiendas.html',{'tiendas':tiendas})

def crear_cliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
           Cliente.objects.create(
               nombre = form.cleaned_data['nombre'],
               email = form.cleaned_data ['correo']
           )
           return redirect('listar_clientes')#se pone el name de urls 
        
    else:
        form = clienteForm()
        return render(request, 'nuevo_cliente.html',{'form':form})
        
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    cliente.delete()
    redirect('listar_clientes')
    
def artualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data ['correo']
            cliente.save()
            return redirect('listar_clientes')#se pone el name de urls 
    else:
        form = clienteForm(initial={ 
            'nombre': cliente.nombre,
            'correo':cliente.email,
        })
        return render (request, 'actualizar_cliente.html',{'form': form})  
    
#tiendas
def crear_tienda(request):
    if request.method == 'POST':
        form = tiendaForm(request.POST)
        if form.is_valid():
           Tienda.objects.create(
               nombre = form.cleaned_data['nombre'],
               direccion = form.cleaned_data ['direccion']
           )
           return redirect('listar_tiendas')#se pone el name de urls 
        
    else:
        form = tiendaForm()
        return render(request, 'nueva_tienda.html',{'form':form})
    
def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda=id)
    tienda.delete()
    redirect('listar_tiendas')
    
def artualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda = id)
    if request.method == 'POST':
        form = tiendaForm(request.POST)
        if form.is_valid():
            tienda.nombre = form.cleaned_data['nombre']
            tienda.direccion = form.cleaned_data ['direccion']
            tienda.save()
            return redirect('listar_tiendas')#se pone el name de urls 
    else:
        form = clienteForm(initial={ 
            'nombre': tienda.nombre,
            'direccion':tienda.direccion,
        })
        return render (request, 'actualizar_tienda.html',{'form': form})      
    
#CRUD COMPRA
def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'listar_compras.html', {'compras': compras})
    
#crear compra
def crear_compra(request):
    if request.method == 'POST':
        form = compraForm(request.POST)
        if form.is_valid():
            Compra.objects.create(
                fecha=form.cleaned_data['fecha'],
                monto=form.cleaned_data['monto'],
                cliente=form.cleaned_data['cliente'],
                tienda=form.cleaned_data['tienda']
            )
            return redirect('listar_compras')
    else:
        form = compraForm()
        
    return render(request, 'nueva_compra.html', {'form': form})

#eliminar compra
def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    compra.delete()
    return redirect('listar_compras')

#modifica compra   
def actualizar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)

    if request.method == 'POST':
        form = compraForm(request.POST)
        if form.is_valid():
            compra.fecha = form.cleaned_data['fecha']
            compra.monto = form.cleaned_data['monto']
            compra.cliente = form.cleaned_data['cliente']
            compra.tienda = form.cleaned_data['tienda']
            compra.save()
            return redirect('listar_compras')
    else:
        form = compraForm(initial={
            'fecha': compra.fecha,
            'monto': compra.monto,
            'cliente': compra.cliente,
            'tienda': compra.tienda,
        })

    return render(request, 'actualizar_compra.html', {'form': form})
def cerrar_sesion(request):
    logout(request)
    return redirect('login')