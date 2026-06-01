from django.contrib import admin
from .models import (
    Department,
    Employee,
    Computer,
    Vehicle,
    Projector,
    AssetAssignment,
    MaintenanceRecord
)


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Computer)
admin.site.register(Vehicle)
admin.site.register(Projector)
admin.site.register(AssetAssignment)
admin.site.register(MaintenanceRecord)