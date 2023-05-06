from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from core.models import ToDoList
from core.forms import ToDoListForm
from datetime import datetime, timedelta

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):
        nome_tarefa = request.POST.get('nome_tarefa')
        data_tarefa = request.POST.get('data_hora_add')
        if data_tarefa:
            data_formatada = datetime.strptime(data_tarefa, '%Y-%m-%d')
            hoje = datetime.now().replace(minute=0, second=0)
            if data_formatada < hoje - timedelta(days=1):
                erro_date = HttpResponse('Insira apenas datas de hoje em diante!!!')
                erro_date['refresh'] = '3;url=/cadastro/'
                return erro_date

        descricao = request.POST.get('descricao_task')
        dados = {'nome_tarefa': nome_tarefa, 'data_tarefa': data_tarefa, 'descricao': descricao}
        form = ToDoListForm(dados)
        if form.is_valid():
            form.save()
        else:
            erro_form = HttpResponse('Insira todas as informações da tarefa!!!')
            erro_form['refresh'] = '3;url=/cadastro/'
            return erro_form
        
        return redirect('todo_list')

class TaskList(View):
    def get(self, request):
        dados = ToDoList.objects.all()
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
