from django.urls import path, include
from .views import GeoJSONUploadView, GeoJSONMapView, GeoJSONDownloadView, GeoJSONDataListView, GeoJSONDataView, GeoJSONDataEditView, GeoJSONDataDeleteView, GeoJSONAPIExplorerView, GeoJSONDataAddView
from .api.views import GeoJSONDataViewSet
from rest_framework.routers import DefaultRouter

app_name = 'QGIS_Integration_Plugin'

# Set up router for the API views
router = DefaultRouter()
router.register(r'geojsondata', GeoJSONDataViewSet)

urlpatterns = [
    path('upload/', GeoJSONUploadView.as_view(), name='upload'),
    path('map/', GeoJSONMapView.as_view(), name='map'),
    path('download/', GeoJSONDownloadView.as_view(), name='download'),
    path('download/<int:pk>/', GeoJSONDownloadView.as_view(), name='download_single'),
    path('geojsondata_list', GeoJSONDataListView.as_view(), name='list'),
    path('geojson/', GeoJSONDataAddView.as_view(), name='add'),
    path('geojson/<int:pk>/', GeoJSONDataView.as_view(), name='detail'),
    path('geojson/edit/<int:pk>/', GeoJSONDataEditView.as_view(), name='edit_geojson_data'),
    path('geojson/delete/<int:pk>/', GeoJSONDataDeleteView.as_view(), name='delete'),
    path('api-explorer/', GeoJSONAPIExplorerView.as_view(), name='api_explorer'),
    path('api/', include(router.urls)),  # API route for GeoJSON data
]
