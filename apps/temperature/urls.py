from django.urls import path
from . import views

urlpatterns = [
    path('global', views.global_temperature, name='graph')
]