from django.shortcuts import render, redirect
from .forms import EmployeeRegisterForm
from django.contrib import messages
from .models import EmployeeRegister


def employeeRegistration(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeRegisterForm()
        else:
            employee = EmployeeRegister.objects.get(pk=id)
            form = EmployeeRegisterForm(instance=employee)
        return render(request, 'employee/insert.html', {"form": form})
    else:
        if id == 0:
            form = EmployeeRegisterForm(request.POST)
            messages.success(request, "Employee added successfully!")
        else:
            employee = EmployeeRegister.objects.get(pk=id)
            form = EmployeeRegisterForm(request.POST, instance=employee)
            messages.success(request, "Employee updated successfully!")
        if form.is_valid():
            form.save()
        return redirect('show-employee')


def showEmployee(request):
    details = {
       'empDetails': EmployeeRegister.objects.all()
    }
    return render(request, 'employee/show_employee.html', details)


def employeeDelete(request, id):
    form = EmployeeRegister.objects.get(pk=id)
    form.delete()
    return redirect('show-employee')
