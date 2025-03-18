from netbox.filtersets import NetBoxModelFilterSet
from .models import GeoJSONData

class GeoJSONDataFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = GeoJSONData
        fields = ("id", "name", "type", "related_device", "related_circuit", "created_at")

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
