from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_index(request):
    return render(request, 'home/index.html')

