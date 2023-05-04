from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from core.models import ToDoList
from core.forms import ToDoListForm
from datetime import date

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    def post(self, request):
        nome_tarefa = request.POST.get('nome_tarefa')
        data_tarefa = request.POST.get('data_hora_add')
        descricao = request.POST.get('descricao_task')
        dados = {'nome_tarefa': nome_tarefa, 'data_tarefa': data_tarefa, 'descricao': descricao}
        form = ToDoListForm(dados)
        if form.is_valid():
            form.save()
        else:
            erro_form = HttpResponse('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Página de erro</title>
    
    
    <style>
      body .teste{
        font-size: 32px;
        text-align: center;
        margin: 20px 0;
        color: red;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
      }
      body {
  font-family: Arial, sans-serif;
  margin: 0;
}

nav {
  background-color: #d6e4ff;
  height: 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

nav ul {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
}

nav li {
  margin: 0 10px;
}

nav a {
  color: #2a2a2a;
  text-decoration: none;
  font-size: 16px;
  padding: 10px;
  border-radius: 5px;
  transition: color 0.4s ease;
  font-family: 'Pacifico', cursive;
}

nav a:hover {
  color: #6c63ff;
  transition: color 0.4s ease-in-out;
}

nav a.active {
  color: #6c63ff;
}

nav a.icon {
  font-size: 20px;
  margin-right: 5px;
}

nav .logo {
  font-size: 28px;
  color: #6c63ff;
  font-family: 'Sacramento', cursive;
}

nav .logo span {
  font-size: 18px;
  color: #2a2a2a;
}

nav .toggle-nav {
  display: none;
}

@media screen and (max-width: 768px) {
  nav {
    flex-direction: column;
    height: auto;
  }

  nav ul {
    flex-direction: column;
    align-items: center;
  }

  nav li {
    margin: 10px 0;
  }

  nav .toggle-nav {
    display: block;
    font-size: 20px;
    cursor: pointer;
    margin-left: auto;
  }

  nav .toggle-nav:hover {
    color: #6c63ff;
  }

  nav .menu {
    display: none;
    width: 100%;
    text-align: center;
    background-color: #d6e4ff;
    padding: 10px 0;
  }

  nav .menu li {
    display: block;
    margin: 10px 0;
  }

  nav .menu a {
    color: #2a2a2a;
  }

  nav .menu a:hover {
    color: #6c63ff;
  }

  nav .menu a.active {
    color: #6c63ff;
  }
}

nav .btn {
  background-color: #6c63ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 16px;
  width: auto;
  margin: 5px;
  font-size: 16px;
  transition: background-color 0.4s ease;
  cursor: pointer;
  font-family: 'Pacifico', cursive;
}

nav .btn:hover {
  background-color: #fff;
  color: #6c63ff;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
  transform: translateY(-3px);
  transition: background-color 0.4s ease-in-out;

}

nav .btn:hover {
  transform: translateY(2px);

}

nav .btn:focus {
  outline: none;
}
    </style>
    <body>
      <nav>
        <ul>
          <li><a href="todo_list" class="btn">Home</a></li>
          <li><a href="" class="btn">Cadastro</a></li>
        </ul>
      </nav>
        <h1 class="teste">PREENCHA TODOS OS DADOS!!!</h1>
     
    </body>
    </html>''')
            erro_form['Content-Type'] = 'text/html'
            #erro_form['refresh'] = '3;url=/cadastro/'
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
