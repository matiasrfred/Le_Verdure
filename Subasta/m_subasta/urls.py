from django.urls import path
from .views import subastaView


urlpatterns=[
    path('subastas/', subastaView.as_view(), name='subastas_list'),
    path('subastas/<int:id>', subastaView.as_view(), name='subastas_proces')
]