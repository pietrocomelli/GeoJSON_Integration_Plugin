from netbox.filtersets import NetBoxModelFilterSet
from .models import GeoJSONData

# Define the filter set for GeoJSONData model
class GeoJSONDataFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = GeoJSONData  # Specify the model to apply filters on
        fields = ("id", "name", "type", "created_at")  # Fields to filter by

    # Custom search method to filter GeoJSONData by name
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)  # Case-insensitive search by name
