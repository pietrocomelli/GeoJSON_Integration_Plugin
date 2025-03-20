from ..models import GeoJSONData
from .serializers import GeoJSONDataSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class GeoJSONDataViewSet(viewsets.ModelViewSet):
    queryset = GeoJSONData.objects.all()  # Retrieve all GeoJSONData objects
    serializer_class = GeoJSONDataSerializer  # Serializer for GeoJSONData

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["type", "pairs"]  # Fields to filter by
    search_fields = ["name", "description"]  # Fields to search
    ordering_fields = ["created_at"]  # Fields to order by
