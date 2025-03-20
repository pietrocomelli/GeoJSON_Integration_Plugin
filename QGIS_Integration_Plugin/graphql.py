from graphene import ObjectType
from . import graphql
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from .models import GeoJSONData

# Define the GraphQL type for GeoJSONData
class GeoJSONDataType(NetBoxObjectType):
    class Meta:
        model = GeoJSONData  # Specify the model to be used for this GraphQL type
        fields = '__all__'  # Expose all fields of the model

# Define the query class to fetch GeoJSONData
class Query(ObjectType):
    # Field to fetch a single GeoJSONData object
    geojson_data = graphql.ObjectField(GeoJSONDataType)

    # Field to fetch a list of GeoJSONData objects
    geojson_data_list = graphql.ObjectListField(GeoJSONDataType)
