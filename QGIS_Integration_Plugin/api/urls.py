from netbox.api.routers import NetBoxRouter
from .views import GeoJSONDataViewSet

# Create a new router instance for NetBox API
router = NetBoxRouter()

# Register the GeoJSONDataViewSet to the router with the endpoint 'geojsondata'
router.register(r'geojsondata', GeoJSONDataViewSet)

# The router will automatically generate the URLs for the registered viewsets
urlpatterns = router.urls
