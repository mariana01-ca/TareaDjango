from django.shortcuts import render
from .forms import RegistroEquipoForm

def registro_equipo(request):
    equipo = jefe = cantidad = None

    if request.method == 'POST':
        form = RegistroEquipoForm(request.POST)
        if form.is_valid():
            equipo = form.cleaned_data['equipo']
            jefe = form.cleaned_data['jefe']
            cantidad = form.cleaned_data['cantidad']
    else:
        form = RegistroEquipoForm()

    return render(request, 'paticipacion/registro.html', {
        'form': form,
        'equipo': equipo,
        'jefe': jefe,
        'cantidad': cantidad
    })
