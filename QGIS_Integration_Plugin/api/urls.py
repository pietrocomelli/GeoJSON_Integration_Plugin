from netbox.api.routers import NetBoxRouter
from .views import GeoJSONDataViewSet

router = NetBoxRouter()
router.register(r'geojsondata', GeoJSONDataViewSet)

urlpatterns = router.urls
