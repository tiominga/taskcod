from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from utils import sql_to_table
from django.http import JsonResponse

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
            context = {
                'task_data': request.POST,  # Volta para o form mostrando os dados preenchidos:
            }
            return render(request, 'task_form.html', context)
    else:
        return render(request, 'task_form.html')

@login_required
def task_form(request):
    return render(request,'task_form.html')


def task_table(request):
    return render(request,'task_grid.html') #só pro index.html redirecionar para o task_grid.html


def task_sql_to_table(request):    
    sql = "select id,id_clinica as clinica,tipo,prioridade,caminho,descricao,date_format(date_add,'%%d/%%m/%%Y') as Solicitado from task_task order by prioridade"
    params = ''
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


def task_change_priority(request,id_task,priority):
    obj_task = Task(id=id_task)
    obj_task.prioridade = priority
    try:
        obj_task.save(update_fields=['prioridade'])
        return JsonResponse({'status': 'success', 'message': 'Prioridade alterada com sucesso'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})




    