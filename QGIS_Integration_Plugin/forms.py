from django import forms
from .models import GeoJSONData

class GeoJSONDataForm(forms.ModelForm):
    class Meta:
        model = GeoJSONData
        fields = ["name", "description", "type", "pairs", "related_device", "related_circuit", "geometry", "properties"]
        widgets = {
            "geometry": forms.Textarea(attrs={"rows": 4}),
            "properties": forms.Textarea(attrs={"rows": 4}),
        }