from django.urls import path
from .views import lista_tareas, agregar_tarea
urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),
    path('agregar/', agregar_tarea, name='agregar_tarea'),
]