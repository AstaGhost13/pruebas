from django.shortcuts import render,redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'gestion_tareas/lista_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'gestion_tareas/agregar_tarea.html', {'form': form})