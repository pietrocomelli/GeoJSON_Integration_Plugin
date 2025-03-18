from django.urls import path, include
from .views import GeoJSONUploadView, GeoJSONMapView, GeoJSONDownloadView, GeoJSONDataListView, GeoJSONDataView, GeoJSONDataEditView, GeoJSONDataDeleteView, GeoJSONAPIExplorerView
from .api.views import GeoJSONDataViewSet
from netbox.views import generic
from .models import GeoJSONData
from rest_framework.routers import DefaultRouter

app_name = 'QGIS_Integration_Plugin' 


router = DefaultRouter()
router.register(r'geojsondata', GeoJSONDataViewSet)

urlpatterns = [
    path('upload/', GeoJSONUploadView.as_view(), name='upload'),
#    path('api/geojson/', GeoJSONDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='geojsondata'),
    path('map/', GeoJSONMapView.as_view(), name='map'),
    path('download/', GeoJSONDownloadView.as_view(), name='download'),
    path('geojson/', GeoJSONDataListView.as_view(), name='list'),
    path('geojson/<int:pk>/', GeoJSONDataView.as_view(), name='detail'),
    path('geojson/edit/<int:pk>/', GeoJSONDataEditView.as_view(), name='edit'),
    path('geojson/delete/<int:pk>/', GeoJSONDataDeleteView.as_view(), name='delete'),
    path('api-explorer/', GeoJSONAPIExplorerView.as_view(), name='api_explorer'),
    path('api/', include(router.urls)),
]