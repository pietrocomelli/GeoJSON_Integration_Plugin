from rest_framework import serializers
from ..models import GeoJSONData

class GeoJSONDataSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifies the model this serializer is for (GeoJSONData model)
        model = GeoJSONData  
        fields = '__all__'  # This includes every field of the GeoJSONData model
