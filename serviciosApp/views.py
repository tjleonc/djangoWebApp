from django.shortcuts import render
from serviciosApp.models import Servicio


# Create your views here.

def servicios(request):

    servicios = Servicio.objects.all() #importa todos los servicios construidos en el modelo Servicio

    return render(request,'servicios/servicios.html', {'servicios':servicios})