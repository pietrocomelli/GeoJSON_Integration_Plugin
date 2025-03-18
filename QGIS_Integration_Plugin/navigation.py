from netbox.plugins import PluginMenuItem, PluginMenu

menu_items = (
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:list',
        link_text="Elenco GeoJSON",
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:upload',
        link_text='Carica GeoJSON',
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:map',
        link_text='Visualizza Mappa',
    ),
    PluginMenuItem(
        link='plugins:QGIS_Integration_Plugin:download',
        link_text="Scarica GeoJSON",
    ),
)

menu = PluginMenu(
    label="QGIS Integration",
    groups=(("Funzionalità", menu_items),),
)