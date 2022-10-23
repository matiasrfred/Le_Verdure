from django.urls import path
from .views import estadisticaView, EstadisticasAllViewset, EstadisticasViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('estadisticas',EstadisticasViewset,EstadisticasAllViewset)
router.register('estadisticas_all',EstadisticasAllViewset)

urlpatterns=[
    path('estadistica/', estadisticaView.as_view(), name='estadistica_list'),
    path('estadistica/<int:id_estad>', estadisticaView.as_view(), name='estadistica_proces')
]