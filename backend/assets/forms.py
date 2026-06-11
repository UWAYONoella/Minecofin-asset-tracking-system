from django import forms
from .models import Computer
from .models import AssetAssignment
from .models import Employee
from .models import Vehicle
from .models import Projector


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

    def clean(self):
        cleaned_data = super().clean()

        computer = cleaned_data.get('computer')
        vehicle = cleaned_data.get('vehicle')
        projector = cleaned_data.get('projector')

        # Check Computer
        if computer and computer.status == "Assigned":
            raise forms.ValidationError(
                f"Computer {computer.asset_tag} is already assigned."
            )

        # Check Vehicle
        if vehicle and vehicle.status == "Assigned":
            raise forms.ValidationError(
                f"Vehicle {vehicle.plate_number} is already assigned."
            )

        # Check Projector
        if projector and projector.status == "Assigned":
            raise forms.ValidationError(
                f"Projector {projector.asset_tag} is already assigned."
            )

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['computer'].queryset = Computer.objects.filter(
            status='Available'
        )

        self.fields['vehicle'].queryset = Vehicle.objects.filter(
            status='Available'
        )

        self.fields['projector'].queryset = Projector.objects.filter(
            status='Available'
        )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'phone', 'department']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'plate_number',
            'brand',
            'model',
            'purchase_date',
            'status']      

        
class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = [
            'asset_tag',
            'brand',
            'serial_number',
            'purchase_date',
            'status'
        ]