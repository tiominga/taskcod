from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages

@login_required
def task_add(request):
    if request.method == 'POST':
        task = Task(
            cod_user=request.user.id,
            id_clinica=request.POST.get('id_clinica'),
            tipo=request.POST.get('tipo'),
            prioridade=request.POST.get('prioridade'),
            caminho=request.POST.get('caminho'),
            descricao=request.POST.get('descricao')
        )
        try:
            task.full_clean()
            task.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('print:print_form', cod_task=task.id)
        except Exception as e:
            messages.error(request, e.messages[0])
            # Volta para o form mostrando os dados preenchidos:
            context = {
                'task_data': request.POST,
            }
            return render(request, 'task_form.html', context)
    else:
        return render(request, 'task_form.html')

@login_required
def task_form(request):
    return render(request,'task_form.html')