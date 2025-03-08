from extras.plugins import PluginMenuItem, PluginMenu

menu_items = (
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:upload',
        link_text='Carica GeoJSON',
        permissions=['QGIS_Integration_Plugin.view_geojsondata'],
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:map',
        link_text='Visualizza Mappa',
        permissions=['QGIS_Integration_Plugin.view_geojsondata'],
    ),
)

menu = PluginMenu(
    label="QGIS Integration",
    groups=(("Funzionalità", menu_items),),
)

