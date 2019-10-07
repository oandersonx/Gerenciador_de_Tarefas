from django.shortcuts import render

def listar_tarefas(request):
    return render(request, 'tarefas/listar_tarefas.html')

# Create your views here.
