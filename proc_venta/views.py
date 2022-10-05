from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'proc_venta/home.html')

def pdvext(request):
    return render(request, 'proc_venta/pdvext.html')

def pdvint(request):
    return render(request, 'proc_venta/pdvint.html')

def login(request):
    return render(request, 'proc_venta/login.html')

def pdvopen(request):
    return render(request, 'proc_venta/pdvopen.html')