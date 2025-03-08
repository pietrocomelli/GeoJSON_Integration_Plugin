from django.urls import path
from .views import GeoJSONUploadView, GeoJSONMapView

app_name = "QGIS_Integration_Plugin"

urlpatterns = [
    path("upload/", GeoJSONUploadView.as_view(), name="upload"),
    path("map/", GeoJSONMapView.as_view(), name="map")
]

