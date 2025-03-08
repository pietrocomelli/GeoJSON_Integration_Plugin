import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from extras.models import CustomField
from .models import GeoJSONData

class GeoJSONUploadView(View):
    template_name = "qgis_integration_plugin/upload.html"

    def get(self, request):
        return render(request, self.template_name, {"file_uploaded":False})

    def post(self, request):
        if "geojson_file" not in request.FILES:
            messages.error(request, "Nessun file selezionato.")
            return redirect("plugins:qgis-integration:upload")

        geojson_file = request.FILES["geojson_file"]
        fs = FileSystemStorage(location="/tmp/")
        filename = fs.save(geojson_file.name, geojson_file)
        file_path = fs.path(filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                geojson_data = json.load(f)

            # Controllo che il file sia un GeoJSON valido
            if "features" not in geojson_data:
                messages.error(request, "File GeoJSON non valido.")
                return redirect("plugins:qgis-integration:upload")

            for feature in geojson_data['features']:
                props = feature['properties']
                geometry = feature['geometry']

                try:
                    start_building, end_building = props['name'].split("-")
                except ValueError:
                    messages.error(request, f"Formato del nome errato: {props['name']}")
                    continue

                GeoJSONData.objects.create(
                    name=props.get("name", "Unnamed"),
                    type=props.get("type", "Unknown"),
                    pairs=props.get("pairs",0),
                    geometry=geometry,
                    properties=props,
                )

            # Qui puoi salvare i dati in NetBox (ad esempio creando oggetti Custom)
            messages.success(request, "File GeoJSON caricato con successo e dati salvati in Netbox!")
            return render(request, self.template_name, {"file_uploaded": True})

        except json.JSONDecodeError:
            messages.error(request, "Errore nella lettura del file GeoJSON.")
            return redirect("plugins:qgis-integration:upload")

class GeoJSONMapView(View):
    template_name = "qgis_integration_plugin/map.html"

    def get(self,request):
        # Otteniamo tutte le connessioni dal database
        connections = GeoJSONData.objects.all()
        return render(request, self.template_name, {'connections':connections})
