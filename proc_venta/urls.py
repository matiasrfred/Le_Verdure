from django.urls import path
from .views import home, pdvext, pdvint, login, pdvopen

urlpatterns = [
    path('', home, name="home"),
    path('pdvext/', pdvext, name="pdvext"),
    path('pdvint/', pdvint, name="pdvint"),
    path('login/', login, name="login"),
    path('pdvopen/', pdvopen, name="pdvopen"),
]
