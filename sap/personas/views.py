from django.shortcuts import render, get_object_or_404, redirect
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


# Persona
def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


def nuevaPersona(request):
    if request.method == 'POST':  # Verificar si la petición es mediante el método POST
        formaPersona = PersonaForm(request.POST)  # Crea una instancia del formulario utilizando los datos de POST
        if formaPersona.is_valid():   # Verificar si los datos ingresados en el formulario son válidos
            formaPersona.save()  # Guardar la instancia del formulario en la DB
            return redirect('index')  # Redireccionar al usuario a la página de inicio ('index')
    else:
        formaPersona = PersonaForm()  # Crea una instancia vacía del formulario

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')


# Domicilio
def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio})


def nuevaDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})


def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('index')
