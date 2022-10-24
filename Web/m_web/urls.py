from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('pdvext/', pdvext, name="pdvext"),
    path('login/', login, name="login"),
    path('productores/', productores, name="productores"),
    path('productos/', productos, name="productos"),
    path('subasta/', subasta, name="subasta"),
    
]
