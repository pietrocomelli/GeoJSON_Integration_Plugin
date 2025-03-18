from rest_framework import serializers
from ..models import GeoJSONData

class GeoJSONDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJSONData
        fields = '__all__'
