from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from django.http import JsonResponse
import json


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
            data = {'success':True,'message':task.id}             
        except Exception as e:
            data = {'success':False,'message':e.messages[0]}             
    return JsonResponse(data)      

    

@login_required
def task_form(request):
    return render(request,'task_form.html')