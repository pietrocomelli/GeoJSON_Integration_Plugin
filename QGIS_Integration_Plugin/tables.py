import django_tables2 as tables
from .models import GeoJSONData

class GeoJSONDataTable(tables.Table):
    name = tables.Column(linkify=True)  # Link alla vista dettaglio
    type = tables.Column()
    pairs = tables.Column()
    related_device = tables.Column(linkify=True)  # Link ai dispositivi NetBox
    related_circuit = tables.Column(linkify=True)  # Link ai circuiti NetBox
    created_at = tables.DateTimeColumn(format="Y-m-d H:i")

    class Meta:
        model = GeoJSONData
        fields = ("name", "type", "pairs", "related_device", "related_circuit", "created_at")
        attrs = {"class": "table table-striped table-hover"}
