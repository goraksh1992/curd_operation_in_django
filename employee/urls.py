from django.urls import path
from .views import employeeRegistration, showEmployee, employeeDelete

urlpatterns = [
    path('', employeeRegistration, name="insert_employee"),
    path('<int:id>/', employeeRegistration, name="update_employee"),
    path('show-employee', showEmployee, name="show-employee"),
    path('delete_employee/<int:id>', employeeDelete, name="delete_employee"),
]