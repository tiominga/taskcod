from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages

@login_required
def task_add(request):
    if request.method == 'POST':
        task = Task(
            cod_user=request.user.id,
            id_clinica=request.POST['id_clinica'],
            tipo=request.POST['tipo'],
            prioridade=request.POST['prioridade'],
            caminho=request.POST['caminho'],
            descricao=request.POST['descricao']
        )
        try:
            task.full_clean()
            task.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('task:task_form')
        except Exception as e:
            messages.error(request, str(e))
    return redirect('task:task_form')

@login_required
def task_form(request):
    return render(request,'task_form.html')