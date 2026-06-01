from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Computer(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Maintenance', 'Maintenance'),
    ]

    asset_tag = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.asset_tag


class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Maintenance', 'Maintenance'),
    ]

    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.plate_number


class Projector(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Maintenance', 'Maintenance'),
    ]

    asset_tag = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.asset_tag


class AssetAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    computer = models.ForeignKey(
        Computer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    projector = models.ForeignKey(
        Projector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Assignment to {self.employee.full_name}"


class MaintenanceRecord(models.Model):
    description = models.TextField()
    maintenance_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    computer = models.ForeignKey(
        Computer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    projector = models.ForeignKey(
        Projector,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Maintenance on {self.maintenance_date}"