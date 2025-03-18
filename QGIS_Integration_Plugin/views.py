import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from netbox.views import generic
from .models import GeoJSONData
from .tables import GeoJSONDataTable
from .forms import GeoJSONDataForm

class GeoJSONUploadView(View):
    template_name = "qgis_integration_plugin/upload.html"

    def get(self, request):
        return render(request, self.template_name, {"file_uploaded": False})

    def post(self, request):
        if "geojson_file" not in request.FILES:
            messages.error(request, "Nessun file selezionato.")
            return redirect("plugins:QGIS_Integration_Plugin:upload")

        geojson_file = request.FILES["geojson_file"]
        fs = FileSystemStorage(location="/tmp/")
        filename = fs.save(geojson_file.name, geojson_file)
        file_path = fs.path(filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                geojson_data = json.load(f)

            if "features" not in geojson_data:
                messages.error(request, "File GeoJSON non valido.")
                return redirect("plugins:QGIS_Integration_Plugin:upload")

            for feature in geojson_data["features"]:
                props = feature.get("properties", {})
                geometry = feature.get("geometry", {})

                if not geometry:
                    messages.warning(request, "Feature senza geometria, ignorata.")
                    continue

                name = props.get("name", "Unnamed")
                fiber_type = props.get("type", "Unknown")
                pairs = props.get("pairs", 0)
                coordinates = geometry.get("coordinates", [])

                if GeoJSONData.objects.filter(name=name, type=fiber_type).exists():
                    messages.warning(request, f"Il dato con nome '{name}' e tipo '{fiber_type}' esiste già nel database. Ignorato.")
                    continue

                GeoJSONData.objects.create(
                    name=name,
                    type=fiber_type,
                    pairs=pairs,
                    geometry=geometry,
                    properties=props,
                )

            messages.success(request, "File GeoJSON caricato con successo!")
            return render(request, self.template_name, {"file_uploaded": True})

        except json.JSONDecodeError:
            messages.error(request, "Errore nella lettura del file GeoJSON.")
            return redirect("plugins:QGIS_Integration_Plugin:upload")




class GeoJSONMapView(View):
    template_name = "qgis_integration_plugin/map.html"

    def get(self, request):
        connections = GeoJSONData.objects.all()
        return render(request, self.template_name, {"connections": connections})


class GeoJSONDownloadView(View):
    def get(self, request):
        data = GeoJSONData.objects.all()
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": entry.geometry,
                    "properties": entry.properties,
                }
                for entry in data
            ],
        }

        response = HttpResponse(json.dumps(geojson, indent=4), content_type="application/json")
        response["Content-Disposition"] = 'attachment; filename="export.geojson"'
        return response

class GeoJSONDataListView(generic.ObjectListView):
    queryset = GeoJSONData.objects.all()
    table = GeoJSONDataTable
    template_name = "netbox/generic/object_list.html"

class GeoJSONDataView(generic.ObjectView):
    queryset = GeoJSONData.objects.all()

class GeoJSONDataEditView(generic.ObjectEditView):
    queryset = GeoJSONData.objects.all()
    model_form = GeoJSONDataForm
    template_name = "qgis_integration_plugin/edit_geojson_data.html"
    
    def get(self, request, pk):
        # Recupera il dato GeoJSON da modificare
        geojson_data = get_object_or_404(GeoJSONData, pk=pk)
        form = GeoJSONDataForm(instance=geojson_data)
        return render(request, self.template_name, {'form': form, 'geojson_data': geojson_data})
    
    def post(self, request, pk):
        geojson_data = get_object_or_404(GeoJSONData, pk=pk)
        form = GeoJSONDataForm(request.POST, instance=geojson_data)
        
        if form.is_valid():
            form.save()  # Salva le modifiche
            messages.success(request, "Dati aggiornati con successo!")
            return redirect('QGIS_Integration_Plugin:api_explorer')  # Ritorna all'esplorazione dei dati
        else:
            messages.error(request, "Errore nel salvataggio dei dati.")
            return render(request, self.template_name, {'form': form, 'geojson_data': geojson_data})


class GeoJSONDataDeleteView(generic.ObjectDeleteView):
    queryset = GeoJSONData.objects.all()

    def post(self, request, pk):
        # Verifica se il metodo del form è DELETE
        if request.POST.get('_method') == 'DELETE':
            data = get_object_or_404(GeoJSONData, pk=pk)
            data.delete()
            messages.success(request, "Dato eliminato con successo!")
            return redirect('QGIS_Integration_Plugin:api_explorer')
        else:
            # Se non è DELETE, reindirizza
            return redirect('QGIS_Integration_Plugin:api_explorer')

class GeoJSONAPIExplorerView(View):
    template_name = "qgis_integration_plugin/api_explorer.html"

    def get(self, request):
        geojson_data = GeoJSONData.objects.all()
        return render(request, self.template_name, {"geojson_data": geojson_data})