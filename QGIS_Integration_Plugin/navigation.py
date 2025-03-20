from netbox.plugins import PluginMenuButton, PluginMenuItem
from extras.choices import ButtonColorChoices

# Define a button for GeoJSON data actions
geojsondata_buttons = [
    PluginMenuButton(
        link='plugins:QGIS_Integration_Plugin:upload',
        title='Import',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

# Define menu items with the respective buttons
menu_items = (
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:upload',
        link_text='GeoJSON Data Upload',
        buttons=geojsondata_buttons
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:api_explorer',
        link_text='API Explorer',
        buttons=geojsondata_buttons
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:map',
        link_text='Map',
        buttons=geojsondata_buttons
    ),
)
