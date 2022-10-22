from django.urls import path
from .views import usuarioView


urlpatterns=[
    path('usuarios/', usuarioView.as_view(), name='usuarios_list'),
    path('usuarios/<int:id>', usuarioView.as_view(), name='usuarios_proces')
]