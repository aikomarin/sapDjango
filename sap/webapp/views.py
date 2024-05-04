from django.shortcuts import render
from personas.models import Persona, Domicilio


def bienvenido(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'bienvenido.html', {
        'no_personas': no_personas, 'personas': personas,
        'no_domicilios': no_domicilios, 'domicilios': domicilios})
