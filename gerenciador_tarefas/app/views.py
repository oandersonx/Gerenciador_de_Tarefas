from django.shortcuts import render

def listar_tarefas(request):
    return render(request, 'tarefas/lista_tarefas.html')

# Create your views here.
