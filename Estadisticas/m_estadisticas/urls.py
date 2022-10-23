from django.urls import path
from .views import estadisticaView


urlpatterns=[
    path('estadistica/', estadisticaView.as_view(), name='estadistica_list'),
    path('estadistica/<int:id>', estadisticaView.as_view(), name='estadistica_proces')
]