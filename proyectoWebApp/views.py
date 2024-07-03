from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'ProyectoWebApp/index.html')

def tienda(request):
    return render(request,'ProyectoWebApp/tienda.html')

def blog(request):
    return render(request,'ProyectoWebApp/blog.html')



