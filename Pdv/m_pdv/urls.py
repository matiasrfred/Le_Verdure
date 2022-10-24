from unicodedata import name
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('pdvs',PdvViewset,PdvAllViewset)
router.register('pdvs_all',PdvAllViewset)
router.register('estadopdvs',EstadopdvViewset,EstadopdvAllViewset)
router.register('estadopdvs_all',EstadopdvAllViewset)
router.register('ofertantes',OfertanteViewset,OfertanteAllViewset)
router.register('ofertantes_all',OfertanteAllViewset)


urlpatterns=[
    path('pdvs/', pdvView.as_view(), name='pdvs_list'),
    path('pdvs/<int:id_pdv>', pdvView.as_view(), name='pdvs_proces'),
    path('ofertantes/', ofertanteView.as_view(), name='ofertantes_proces'),
    path('ofertantes/<int:id_oferta>',ofertanteView.as_view(), name='ofertantes_proces'),
    path('estadopdvs/',estadopdvView.as_view(), name="estadopdv_list"),
    path('estadopdvs/<int:id_estadopdv>', estadopdvView.as_view(), name='estadopdvs_proces')
]