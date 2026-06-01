from django import forms
from .models import Computer


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