from django.db import models
from netbox.models import PrimaryModel 
from dcim.models import Device
from circuits.models import Circuit
from django.urls import reverse

class GeoJSONData(PrimaryModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    pairs = models.IntegerField()
    geometry = models.JSONField()
    properties = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    related_device = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Dispositivo associato, se applicabile."
    )
    related_circuit = models.ForeignKey(
        Circuit, on_delete=models.SET_NULL, null=True, blank=True, 
        help_text="Circuito associato, se applicabile."
    )
    
    custom_field_data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.name} ({self.type})"


