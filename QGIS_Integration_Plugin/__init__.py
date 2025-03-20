from netbox.plugins import PluginConfig

# Define the plugin configuration class for QGIS Integration
class QGISIntegrationPluginConfig(PluginConfig):
    name = "QGIS_Integration_Plugin"
    verbose_name = "QGIS Integration Plugin"
    description = "Importa file GeoJSON in NetBox"
    version = "0.1.1"
    base_url = "qgis-integration"
    min_version = "3.5.0"
    
    # No required or default settings for this plugin
    required_settings = []
    default_settings = {}
    
    author = "Pietro Riccardo Comelli"
    author_email = "comelli.pietro@gmail.com"

# Assign the plugin configuration to a variable
config = QGISIntegrationPluginConfig
