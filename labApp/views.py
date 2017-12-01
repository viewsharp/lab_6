from django.shortcuts import render
from django.views.generic import ListView
from .models import *

def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)

class DepartmentsView(ListView):
    model = Departments
    template_name = 'departments.html'
    context_object_name = 'departments_list'



