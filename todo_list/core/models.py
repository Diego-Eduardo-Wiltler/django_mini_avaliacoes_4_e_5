from django.db import models

class ToDoList(models.Model):
    nome_tarefa = models.CharField('nome_tarefa', max_length=150)
    data_tarefa = models.DateField('data_tarefa')
    descricao = models.CharField('descricao', max_length=150)
    data_hora_add = models.DateTimeField('data_hora_add', auto_now_add=True)