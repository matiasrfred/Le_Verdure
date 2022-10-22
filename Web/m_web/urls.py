from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('pdvext/', pdvext, name="pdvext"),
    path('login/', login, name="login"),
    path('pdvopen/', pdvopen, name="pdvopen"),
    path('pdvint/', pdvint, name="pdvint"),
]
