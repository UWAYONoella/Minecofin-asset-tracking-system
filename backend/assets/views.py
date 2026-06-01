from django.shortcuts import render
from .models import Computer, Vehicle, Projector, Employee
from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from .forms import ComputerForm


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