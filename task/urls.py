"""
URL configuration for taskcod project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views

app_name = 'task'


urlpatterns = [

       path('task_form/',views.task_form,name='task_form'),
       path('task_add/',views.task_add,name='task_add'),
       path('task_sql_to_table',views.task_sql_to_table,name='task_sql_to_table'),
       path('task_table',views.task_table,name='task_table'),     
       path('task_change_priority/<int:id_task>/<int:priority>/', views.task_change_priority, name='task_change_priority'),
       
       ] 

