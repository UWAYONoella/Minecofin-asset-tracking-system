from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer, Vehicle, Projector, Employee
from .forms import ComputerForm
from .models import AssetAssignment
from .forms import AssetAssignmentForm
from .models import Employee
from .forms import EmployeeForm
from .forms import VehicleForm


def dashboard(request):
    context = {
        "computers": Computer.objects.count(),
        "vehicles": Vehicle.objects.count(),
        "projectors": Projector.objects.count(),
        "employees": Employee.objects.count(),
    }

    return render(request, "assets/dashboard.html", context)


def add_computer(request):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm()

    return render(request, 'assets/add_computer.html', {'form': form})


def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'assets/computer_list.html', {'computers': computers})


def edit_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)

# 🚫 BLOCK EDIT IF ASSIGNED
    if computer.status == "Assigned":
        return render(request, 'assets/error.html', {
            'message': 'This computer is assigned and cannot be edited.'
        })
    

    if request.method == "POST":
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm(instance=computer)

    return render(request, 'assets/edit_computer.html', {'form': form})


def delete_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.delete()
    return redirect('computer_list')


def assignment_list(request):
    assignments = AssetAssignment.objects.all()

    return render(
        request,
        'assets/assignment_list.html',
        {'assignments': assignments}
    )


def add_assignment(request):

    if request.method == 'POST':
        form = AssetAssignmentForm(request.POST)

        if form.is_valid():
            assignment = form.save()

            # DEBUG (optional)
            print("Computer:", assignment.computer)

            if assignment.computer_id:
                Computer.objects.filter(id=assignment.computer_id).update(
                    status="Assigned"
                )

            if assignment.vehicle_id:
                Vehicle.objects.filter(id=assignment.vehicle_id).update(
                    status="Assigned"
                )

            if assignment.projector_id:
                Projector.objects.filter(id=assignment.projector_id).update(
                    status="Assigned"
                )

            return redirect('assignment_list')

    else:
        form = AssetAssignmentForm()

    return render(request, 'assets/add_assignment.html', {'form': form})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'assets/add_employee.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'assets/employee_list.html', {'employees': employees})


def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'assets/edit_employee.html', {'form': form})


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')


def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()

    return render(request, 'assets/add_vehicle.html', {'form': form})


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'assets/vehicle_list.html', {'vehicles': vehicles})


def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'assets/edit_vehicle.html', {'form': form})


def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    return redirect('vehicle_list')