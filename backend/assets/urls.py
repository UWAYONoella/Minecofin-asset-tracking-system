from django.urls import path
from .views import add_assignment, assignment_list, dashboard, add_computer, computer_list, edit_computer, delete_computer

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('computers/', computer_list, name='computer_list'),
    path('computers/add/', add_computer, name='add_computer'),
    path('computers/edit/<int:pk>/', edit_computer, name='edit_computer'),
    path('computers/delete/<int:pk>/', delete_computer, name='delete_computer'),
    path(
    'assignments/',
    assignment_list,
    name='assignment_list'
),

path(
    'assignments/add/',
    add_assignment,
    name='add_assignment'
),
]