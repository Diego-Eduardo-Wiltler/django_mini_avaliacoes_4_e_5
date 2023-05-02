from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from core.models import ToDoList
from datetime import date

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    def post(self, request):
        nome_tarefa = request.POST.get('nome_tarefa')
        data_tarefa = request.POST.get('data_hora_add')
        descricao = request.POST.get('descricao_task')
        if not nome_tarefa or not data_tarefa or not descricao:
            return HttpResponse('Preencha todos os campos')
        dados = ToDoList.objects.create(nome_tarefa=nome_tarefa, data_tarefa=data_tarefa, descricao=descricao)
        return redirect('todo_list')

class TaskList(View):
    def get(self, request):
        dados = ToDoList.objects.all()
        if not dados:
            return HttpResponse('Sem Tarefas')
        return render(request, 'todo_list.html', {'dados': dados})

class EditarView(View):
    def get(self, request, id):
        dado = get_object_or_404(ToDoList, id=id)
        return render(request, 'editar.html', {'dado': dado})

    def post(self, request, id):
        dado = get_object_or_404(ToDoList, id=id)
        dado.nome_tarefa = request.POST.get('nome_tarefa')
        dado.data_tarefa = request.POST.get('data_hora_add')
        dado.descricao = request.POST.get('descricao_task')
        dado.save()
        return redirect('todo_list')
    
class DeletarView(View):
    def get(self, request, id):
        dado = get_object_or_404(ToDoList, id=id)
        return render(request, 'deletar.html', {'dado': dado})

    def post(self, request, id):
        dado = get_object_or_404(ToDoList, id=id)
        dado.delete()
        return redirect('todo_list')
