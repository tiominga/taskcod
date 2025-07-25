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
            print(f"id ------->{task.id}")
            return redirect('print:print_form',cod_task = task.id)
        except Exception as e:
              print(f"Erro: {e}")
    return render(request, 'task_form.html')         

    

@login_required
def task_form(request):
    return render(request,'task_form.html')