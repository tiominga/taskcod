from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Print
from django.contrib import messages

# Create your views here.
def print_add(request):
    if request.method == "POST":        
        obj_print = Print(
            cod_task_id = int(request.POST["cod_task"]),
            image = request.FILES["image"]
        )
        try:
            obj_print.full_clean()
            obj_print.save()
            return redirect('print:print_form',cod_task = obj_print.cod_task_id)
        except Exception as e:
             print(f"Erro ao redirecionar: {e}")
    return redirect('print:print_form',cod_task = obj_print.cod_task_id)         

def print_form(request,cod_task):
    return render(request,'print_form.html',{'cod_task':cod_task})


            
