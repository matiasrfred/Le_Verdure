from operator import methodcaller
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'm_web/home.html')

def pdvext(request):
    return render(request, 'm_web/pdvext.html')

def login(request):
    return render(request, 'm_web/login.html')

def productores(request):
    return render(request, 'm_web/productores.html')

def subasta(request):
    return render(request, 'm_web/subasta.html')

def productos(request):
    if request.method == 'POST':
        id_prod = request.POST.get('id-producto')
        

    return render(request, 'm_web/productos.html')

def login(request):
    return render(request, 'm_web/login.html')



