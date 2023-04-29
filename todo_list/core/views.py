from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from core.models import ToDoList

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    def post(self, request):
        nome_tarefa = request.POST.get('nome_tarefa')
        data_tarefa = request.POST.get('data_hora_add')
        descricao = request.POST.get('descricao_task')
        dados = ToDoList.objects.create(nome_tarefa=nome_tarefa, data_tarefa=data_tarefa, descricao=descricao)
        return redirect('todo_list')

class TaskList(View):
    def get(self, request):
        dados = ToDoList.objects.all()
        return render(request, 'todo_list.html', {'dados': dados})
        
    def editar_objeto(request, pk):
        objeto = get_object_or_404(TaskList, pk=pk)
        if request.method == 'POST':
            form = TaskList(request.POST, instance=objeto)
            if form.is_valid():
                form.save()
                return redirect('todo_list')
        else:
            form = TaskList(instance=objeto)
        return render(request, 'editar-objeto.html', {'form': form})

    def deletar_objeto(request, pk):
        objeto = get_object_or_404(TaskList, pk=pk)
        if request.method == 'POST':
            objeto.delete()
            return redirect('todo_list')
        return render(request, 'deletar-objeto.html', {'objeto': objeto})
    
        