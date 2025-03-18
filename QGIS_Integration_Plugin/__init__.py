from netbox.plugins import PluginConfig
from .navigation import menu

class QGISIntegrationPluginConfig(PluginConfig):
    name = "QGIS_Integration_Plugin"
    verbose_name = "QGIS Integration Plugin"
    description = "Importa file GeoJSON in NetBox"
    version = "0.1.1"
    base_url = "qgis-integration"
    min_version = "3.5.0"
    required_settings = []
    default_settings = {}
    #menu_items = (menu,)
    author = "Pietro Riccardo Comelli"
    author_email = "comelli.pietro@gmail.com"

config = QGISIntegrationPluginConfig