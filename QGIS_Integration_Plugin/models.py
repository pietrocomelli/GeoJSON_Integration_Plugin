from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

# Define the GeoJSONData model
class GeoJSONData(NetBoxModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)  # Auto-incrementing primary key
    name = models.CharField(max_length=255)  # Name of the GeoJSON data
    description = models.TextField(blank=True)  # Optional description field
    comments = models.TextField(blank=True)  # Optional comments field
    type = models.CharField(max_length=100)  # Type of the GeoJSON data (e.g., feature type)
    pairs = models.IntegerField()  # Number of pairs (specific to this model's context)
    geometry = models.JSONField()  # Store geometry as JSON
    properties = models.JSONField()  # Store properties as JSON
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the object was created
    created = models.DateTimeField(auto_now_add=True)  # Redundant timestamp field, same as created_at
    custom_field_data = models.JSONField(default=dict, blank=True)  # Custom fields as JSON (optional)

    class Meta:
        ordering = ['name']  # Default ordering by name

    def __str__(self):
        return self.name  # String representation of the object (name field)

    def get_absolute_url(self):
        return reverse('plugins:QGIS_Integration_Plugin:qgis-integration', args=[self.pk])  # URL for the instance detail page
