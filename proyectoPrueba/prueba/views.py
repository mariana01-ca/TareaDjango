from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ClienteForm

# Create your views here.
def saludo(request):
    return HttpResponse("Hola les saluda Django")

def info_usuario(request):
    nombre = "Alan Brito"
    edad = 25
    return HttpResponse(f"Hola soy {nombre} mi edad {edad}")

def saludo_mejorado(request, nombre, edad):
    return HttpResponse(f"Hola soy {nombre} mi edad {edad}")

def tabla_multiplicacion(request):
    num = 5
    resultado = ""
    for i in range(1, 11):
        resultado = resultado + f"{num} x {i} = {num * i}<br>"
    return HttpResponse(resultado)

def saludo2(request):
    datos ={
        'nombre': 'Alan Brito',
        'edad': 25
    }
    return render(request, 'saludo.html', datos)

def info(request):
    return render(request, 'informacion.html')

def nuevo_saludo(request, nombre, edad):
    return render(request, 'nuevo_saludo.html',{'nombre' :nombre, 'edad': edad})

def tabla_producto(request, num):
    lista = []
    for i in range(1,11):
        lista.append({'i': i, 'res': i*num})
        #res = f"<tr><td>{num} * {i}</td> <td> = </td><td>{num * i}</td></tr>"
    return render(request,'tabla_multiplicar.html', {'lista':lista, 'num':num})



