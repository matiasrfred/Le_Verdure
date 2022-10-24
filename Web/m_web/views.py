import email
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.

def home(request):
    return render(request, 'm_web/home.html')

def pdvext(request):
    return render(request, 'm_web/pdvext.html')

def login(request):
    return render(request, 'm_web/login.html')

def pdvopen(request):
    return render(request, 'm_web/pdvopen.html')

def pdvint(request):
    return render(request, 'm_web/pdvint.html')

def solicitudcompra(request):
    return render(request, 'm_web/solicitudcompra.html')




