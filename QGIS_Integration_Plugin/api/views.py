from ..models import GeoJSONData
from .serializers import GeoJSONDataSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class GeoJSONDataViewSet(viewsets.ModelViewSet):
    queryset = GeoJSONData.objects.all()
    serializer_class = GeoJSONDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["type", "pairs", "related_device", "related_circuit"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]
