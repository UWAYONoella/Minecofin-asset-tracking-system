from django import forms
from .models import Computer
from .models import AssetAssignment


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
        fields = [
            'employee',
            'computer',
            'vehicle',
            'projector'
        ]