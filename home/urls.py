from django.contrib import admin
from django.urls import path
from .views import index, graphs, graph_data

urlpatterns = [
    path('', index, name="index"),
    path('graphs/', graphs, name='graphs'),
    path('api/graphs/', graph_data, name='graph_data'),
]
