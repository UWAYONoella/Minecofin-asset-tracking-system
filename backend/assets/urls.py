from django.urls import path
from .views import add_assignment, assignment_list, dashboard, add_computer, computer_list, edit_computer, delete_computer, employee_list, add_employee, edit_employee, delete_employee, add_vehicle, vehicle_list, edit_vehicle, delete_vehicle

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('computers/', computer_list, name='computer_list'),
    path('computers/add/', add_computer, name='add_computer'),
    path('computers/edit/<int:pk>/', edit_computer, name='edit_computer'),
    path('computers/delete/<int:pk>/', delete_computer, name='delete_computer'),
    path('assignments/', assignment_list, name='assignment_list'),
    path('assignments/add/', add_assignment, name='add_assignment'),
path('employees/', employee_list, name='employee_list'),
path('employees/add/', add_employee, name='add_employee'),
path('employees/edit/<int:pk>/', edit_employee, name='edit_employee'),
path('employees/delete/<int:pk>/', delete_employee, name='delete_employee'),
path('vehicles/', vehicle_list, name='vehicle_list'),
path('vehicles/add/', add_vehicle, name='add_vehicle'),
path('vehicles/edit/<int:pk>/', edit_vehicle, name='edit_vehicle'),
path('vehicles/delete/<int:pk>/', delete_vehicle, name='delete_vehicle'),
]

