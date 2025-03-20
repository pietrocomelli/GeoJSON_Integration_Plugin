import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import GeoJSONData

# Table for displaying GeoJSONData
class GeoJSONDataTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    pairs = tables.Column()
    related_device = tables.Column(linkify=True)
    related_circuit = tables.Column(linkify=True)
    created_at = tables.DateTimeColumn()

    class Meta(NetBoxTable.Meta):
        # Meta class to define model and table display settings
        model = GeoJSONData
        fields = ('name', 'type', 'pairs', 'created_at', 'comments', 'actions')
        default_columns = ('name', 'pairs', 'type')
