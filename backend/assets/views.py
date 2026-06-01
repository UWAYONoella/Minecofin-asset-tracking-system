from django.shortcuts import render
from .models import Computer, Vehicle, Projector, Employee
from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from .forms import ComputerForm
from .models import AssetAssignment
from .forms import AssetAssignmentForm


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
            form.save()
            return redirect('assignment_list')

    else:
        form = AssetAssignmentForm()

    return render(
        request,
        'assets/add_assignment.html',
        {'form': form}
    )