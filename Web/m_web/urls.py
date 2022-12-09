from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('pdvext/', pdvext, name="pdvext"),
    path('pdv_id/<str:id_pdv>', pdv_id, name="pdvext_id"),
    path('login/', login, name="login"),
    path('transportista/', transportista, name="transportista"),
    path('productos/', productos, name="productos"),
    path('subasta/', subasta, name="subasta"),
    path('solicitud_compra/', solicitud_compra, name="solicitud_compra"),
    path('lista_pdv/<str:id_pdv>', lista_pdv, name="lista_pdv"),
    path('cap_transporte/', cap_transporte, name="cap_transporte"),
    
]
