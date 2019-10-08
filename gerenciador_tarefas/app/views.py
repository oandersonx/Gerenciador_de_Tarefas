from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades.tarefa import Tarefa
from .services import tarefa_service

def listar_tarefa(request):
    nome_tarefa = "Passando essa tarefa pelo metodo da view"
    return render(request, 'tarefas/listar_tarefa.html', {"nome_tarefa":nome_tarefa})


def cadastar_tarefa(request):
    if request.method == "POST": #Se clicar no botao "Salvar"
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid(): #Se as informacoes digitadas estiverem OK
            titulo = form_tarefa.cleaned_data["titulo"]
            descricao= form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]
            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao,data_expiracao=data_expiracao,prioridade=prioridade)
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect("listar_tarefa") #Volta para página "/listar_tarefa"
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html',{"form_tarefa": form_tarefa})


# Create your views here.
