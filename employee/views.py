from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


class EmployeeList(ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'emp_list.html'
    context_object_name = 'employee'


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'general.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employees_list')

class EmployeeDetail(DetailView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'detail.html'
    context_object_name = 'employee'

class DeleteEmployee(DeleteView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employees_list')

