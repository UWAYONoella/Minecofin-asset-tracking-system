from django.shortcuts import render
from .models import Computer, Vehicle, Projector, Employee


def dashboard(request):
    context = {
        "computers": Computer.objects.count(),
        "vehicles": Vehicle.objects.count(),
        "projectors": Projector.objects.count(),
        "employees": Employee.objects.count(),
    }

    return render(request, "assets/dashboard.html", context)