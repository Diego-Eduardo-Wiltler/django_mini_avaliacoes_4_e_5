from django.urls import path, include
from . import views
from .views import CadastroView, TaskList

urlpatterns = [
    path('todo_list', TaskList.as_view(), name='todo_list'),
    path('cadastro', CadastroView.as_view(), name='cadastro')
]
