from django.contrib import admin
from .models import GeoJSONData

@admin.register(GeoJSONData)
class GeoJSONDataAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "pairs", "related_device", "related_circuit", "created")
    search_fields = ("name", "type")