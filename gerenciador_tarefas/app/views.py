from django.shortcuts import render

def listar_tarefas(request):
    nome_tarefa = "Passando essa tarefa pelo metodo da view"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa":nome_tarefa})

# Create your views here.
