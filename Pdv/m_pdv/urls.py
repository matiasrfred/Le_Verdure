from unicodedata import name
from django.urls import path
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register('pdv',PdvViewset,PdvAllViewset)
router.register('pdv_all',PdvAllViewset)


urlpatterns=[
    path('pdvs/', pdvView.as_view(), name='pdvs_list'),
    path('pdvs/<int:id>', pdvView.as_view(), name='pdvs_proces'),
    path('ofertantes/', ofertanteView.as_view(), name='ofertantes_proces'),
    path('ofertantes/<int:id>',ofertanteView.as_view(), name='ofertantes_proces'),
    path('estadopdvs/',estadopdvView.as_view(), name="estadopdv_list"),
    path('estadopdvs/<int:id>', estadopdvView.as_view(), name='estadopdvs_proces')
]