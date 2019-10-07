from django.shortcuts import render
from .forms import TarefaForm

def listar_tarefa(request):
    nome_tarefa = "Passando essa tarefa pelo metodo da view"
    return render(request, 'tarefas/listar_tarefa.html', {"nome_tarefa":nome_tarefa})


def cadastar_tarefa(request):
    form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html',{"form_tarefa": form_tarefa})


# Create your views here.
