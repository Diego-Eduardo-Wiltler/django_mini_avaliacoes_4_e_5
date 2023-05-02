from django.urls import path
from core.views import CadastroView, TaskList, EditarView, DeletarView

urlpatterns = [
    path('', TaskList.as_view(), name='todo_list'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('editar/<int:id>/', EditarView.as_view(), name='editar'),
    path('deletar/<int:id>/', DeletarView.as_view(), name='deletar'),
]
