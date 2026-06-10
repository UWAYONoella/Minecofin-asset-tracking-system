from django import forms
from .models import Computer
from .models import AssetAssignment
from .models import Employee
from .models import Vehicle

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = [
            'asset_tag',
            'brand',
            'model',
            'serial_number',
            'purchase_date',
            'status'
        ]


class AssetAssignmentForm(forms.ModelForm):
    class Meta:
        model = AssetAssignment
        fields = ['employee', 'computer', 'vehicle', 'projector']

    def clean_computer(self):
        computer = self.cleaned_data.get('computer')

        if computer and computer.status == "Assigned":
            raise forms.ValidationError("This computer is already assigned!")

        return computer


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'phone', 'department']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['asset_tag', 'brand', 'model']