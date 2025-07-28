from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from utils import sql_to_table
from django.http import JsonResponse
from dev.models import Dev

@login_required
def task_add(request):    
    if request.method == 'POST':

        id_task = request.POST.get('id')

        if id_task:        
            obj_task = Task.objects.get(id=id_task)
        else:
            obj_task = Task()

        obj_task.cod_user = request.user.id
        obj_task.id_clinica = request.POST.get('id_clinica')
        obj_task.tipo = request.POST.get('tipo')
        obj_task.prioridade = request.POST.get('prioridade')
        obj_task.caminho = request.POST.get('caminho')
        obj_task.descricao = request.POST.get('descricao')
        obj_task.cod_dev = request.POST.get('dev')
        
        
        try:
            obj_task.full_clean()
            obj_task.save()
            messages.success(request, 'Tarefa salva com sucesso!')
            return redirect('print:print_form', cod_task=obj_task.id)
        except Exception as e:
            obj_dev = Dev.objects.all()
            messages.error(request, e.messages[0])           
            context = {
                'task_data': request.POST,  # Volta para o form mostrando os dados preenchidos:
                'devs': obj_dev,
            }
            return render(request, 'task_form.html', context)
    else:
        return render(request, 'task_form.html')

@login_required
def task_form(request):
    obj_dev = Dev.objects.all()
    return render(request,'task_form.html',{'devs':obj_dev})

@login_required
def task_table(request):
    obj_dev = Dev.objects.all()
    return render(request,'task_grid.html',{'devs':obj_dev}) #só pro index.html redirecionar para o task_grid.html

@login_required
def task_sql_to_table(request):    
    sql = """
    select 
    t.id,
    t.id_clinica as 'Clínica',
    t.Tipo,
    t.Prioridade,
    u.username as Solicitante,
    d.name as Executor,
    t.Caminho,
    t.descricao as 'Descrição',
    date_format(t.date_add,'%%d/%%m/%%Y') as Solicitado 
    from 
    task_task as t,
    auth_user as u,
    dev_dev as d 
    where 
    u.id=t.cod_user
    and
    d.id = t.cod_dev
    and prioridade like %s 
    and cod_dev like %s    
    order by t.prioridade"""

    if request.method == "POST":     
        param_prioridade = request.POST.get("prioridade")
        param_dev = request.POST.get("dev")

    if param_prioridade:    
        params = [param_prioridade,param_dev]
    else:    
        params = '%'

    edit_function = 'edit_task'
    delete_function = 'delete_task'
    tr_function = 'tr_click'
    pagination = 10
    style_index = request.POST.get('style_table', 0)
    
    offset = request.POST.get('offset', 0)

    # Convert the SQL query to a table
    obj_sql_to_table = sql_to_table.SqlToTable()
    obj_sql_to_table.set_query(sql)
    obj_sql_to_table.set_params(params)
    obj_sql_to_table.set_edit_function(edit_function)
    obj_sql_to_table.set_delete_function(delete_function)
    obj_sql_to_table.set_tr_function(tr_function)
    obj_sql_to_table.set_pagination(pagination)
    obj_sql_to_table.set_offset(offset)
    obj_sql_to_table.set_style_index(style_index)

    table = obj_sql_to_table.query_to_html()  

    # Render the table in the template
    return JsonResponse({'status':'success','table':table})

@login_required
def task_change_priority(request,id_task,priority):
    obj_task = Task(id=id_task)
    obj_task.prioridade = priority
    try:
        obj_task.save(update_fields=['prioridade'])
        return JsonResponse({'status': 'success', 'message': 'Prioridade alterada com sucesso'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@login_required    
def task_edit(request,id_task):
    obj_dev = Dev.objects.all()  
    obj_task = Task.objects.get(id = id_task)
    return render(request,'task_form.html',{'task_data':obj_task,'devs':obj_dev})


def task_delete(request, id_task):
    try:
        obj_task = Task.objects.get(id=id_task)
        obj_task.delete()
        return JsonResponse({'status': 'success','message' : 'Tarefa apagada'})
    except Task.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Tarefa não encontrada'})





    