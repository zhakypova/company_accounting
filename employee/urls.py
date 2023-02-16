from django.contrib import admin
from django.urls import path
from .views import EmployeeList, EmployeeCreate, EmployeeDetail, DeleteEmployee

urlpatterns = [
    path('', EmployeeList.as_view(), name='employees_list'),
    path('create/', EmployeeCreate.as_view(), name='employee_create'),
    path('<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('<int:pk>/delete/', DeleteEmployee.as_view(), name='delete'),

]