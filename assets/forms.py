from django import forms 
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'serial_no',
            'asset_categroy',
            'asset_type',
            'owner',
            'department',
            'status',
            'notes',
        ]
        
        widgets = {
            'notes': forms.Textarea(attrs={'rows'}),
            'status': forms.Select(choices=Asset.STATUS_CHOICES),
        }