from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_tarefa/', listar_tarefa, name='listar_tarefa'),
    path('cadastrar_tarefa/', cadastar_tarefa, name='cadastrar_tarefa')
]
