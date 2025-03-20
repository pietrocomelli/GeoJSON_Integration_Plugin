import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db import transaction
from django.core.files.storage import FileSystemStorage
from netbox.views import generic
from .models import GeoJSONData
from .tables import GeoJSONDataTable
from .forms import GeoJSONDataForm

# View for handling GeoJSON file upload
class GeoJSONUploadView(View):
    queryset = GeoJSONData.objects.all()
    template_name = "qgis_integration_plugin/upload.html"

    def get(self, request):
        # Renders the upload page. Initially, no file has been uploaded.
        return render(request, self.template_name, {"file_uploaded": False})

    def post(self, request):
        # Handles the file upload process
        if "geojson_file" not in request.FILES:
            messages.error(request, "No file selected.")
            return redirect("plugins:QGIS_Integration_Plugin:upload")

        # Save the uploaded GeoJSON file to the temporary storage location
        geojson_file = request.FILES["geojson_file"]
        fs = FileSystemStorage(location="/tmp/")
        filename = fs.save(geojson_file.name, geojson_file)
        file_path = fs.path(filename)

        try:
            # Open and load the content of the uploaded GeoJSON file
            with open(file_path, "r", encoding="utf-8") as f:
                geojson_data = json.load(f)

            # Ensure that the file contains the expected "features" key
            if "features" not in geojson_data:
                messages.error(request, "Invalid GeoJSON file.")
                return redirect("plugins:QGIS_Integration_Plugin:upload")

            # Loop through each feature in the GeoJSON data
            for feature in geojson_data["features"]:
                props = feature.get("properties", {})
                geometry = feature.get("geometry", {})

                if not geometry:
                    messages.warning(request, "Feature without geometry, ignored.")
                    continue  # Skip this feature if no geometry is found

                # Extract relevant data from the feature's properties and geometry
                name = props.get("name", "Unnamed")
                description = props.get("description", "")
                comments = props.get("comments", "")
                fiber_type = props.get("type", "Unknown")
                pairs = props.get("pairs", 0)
                coordinates = geometry.get("coordinates", [])
                custom_field_data = props.get("custom_field_data", {})

                # Check if a record already exists with the same name
                if GeoJSONData.objects.filter(name=name).exists():
                    existing_entry = GeoJSONData.objects.get(name=name)

                    # Compare the fields one by one to check if any field differs
                    if (existing_entry.description != description or
                        existing_entry.comments != comments or
                        existing_entry.type != fiber_type or
                        existing_entry.pairs != pairs or
                        existing_entry.geometry != geometry or
                        existing_entry.properties != props or
                        existing_entry.custom_field_data != custom_field_data):
                        
                        # At least one field is different, so create a new entry
                        GeoJSONData.objects.create(
                            name=name,
                            description=description,
                            comments=comments,
                            type=fiber_type,
                            pairs=pairs,
                            geometry=geometry,
                            properties=props,
                            custom_field_data=custom_field_data
                        )
                    else:
                        messages.warning(request, f"Entry '{name}' already exists with identical fields, skipped.")
                        continue  # Skip if all fields are the same
                else:
                    # If no existing record with the same name, create a new one
                    GeoJSONData.objects.create(
                        name=name,
                        description=description,
                        comments=comments,
                        type=fiber_type,
                        pairs=pairs,
                        geometry=geometry,
                        properties=props,
                        custom_field_data=custom_field_data
                    )

            # Success message and redirect to the API explorer page
            messages.success(request, "GeoJSON file uploaded successfully!")
            return redirect("plugins:QGIS_Integration_Plugin:api_explorer")

        except json.JSONDecodeError:
            # Handle errors related to invalid JSON structure
            messages.error(request, "Error reading the GeoJSON file.")
            return redirect("plugins:QGIS_Integration_Plugin:upload")

# View for displaying GeoJSON data on a map
class GeoJSONMapView(View):
    template_name = "qgis_integration_plugin/map.html"

    def get(self, request):
        """Show all GeoJSON data on the map"""
        connections = GeoJSONData.objects.all()
        return render(request, self.template_name, {"connections": connections, "filtered": False})

    def post(self, request):
        """Show only selected GeoJSON data on the map based on user input"""
        selected_ids = request.POST.get("selected_rows")

        if selected_ids:
            # If specific rows are selected, filter the data based on the IDs
            selected_ids = selected_ids.split(",")
            connections = GeoJSONData.objects.filter(pk__in=selected_ids)
        else:
            # No selection, show no data
            connections = GeoJSONData.objects.none()

        return render(request, self.template_name, {"connections": connections, "filtered": True})

# View for downloading GeoJSON data
class GeoJSONDownloadView(View):
    queryset = GeoJSONData.objects.all()

    def get(self, request, pk=None):
        """Handle the download of the GeoJSON data. If a specific pk is provided, download that particular entry."""
        if pk:
            data = [get_object_or_404(GeoJSONData, pk=pk)]
        else:
            # If no pk is provided, fetch the latest data based on the last updated timestamp
            data = GeoJSONData.objects.order_by('-last_updated')

        # Construct the GeoJSON structure for export
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "id": entry.id,
                        "name": entry.name,
                        "type": entry.type,
                        "pairs": entry.pairs,
                        "description": entry.description,
                        "last_updated": entry.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
                    },
                    "geometry": {
                        "type": entry.geometry["type"],
                        "coordinates": entry.geometry["coordinates"],
                    },
                }
                for entry in data
            ],
        }

        # Set the appropriate filename for the download response
        filename = f"geojson_{pk}.geojson" if pk else "export.geojson"
        response = HttpResponse(json.dumps(geojson, indent=4), content_type="application/json")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response

# View for listing GeoJSON data
class GeoJSONDataListView(generic.ObjectListView):
    queryset = GeoJSONData.objects.all()
    table = GeoJSONDataTable
    template_name = "qgis_integration_plugin/geojsondata_list.html"

# View for displaying details of a single GeoJSON entry
class GeoJSONDataView(generic.ObjectView):
    queryset = GeoJSONData.objects.all()

# View for editing a GeoJSON entry
class GeoJSONDataEditView(generic.ObjectEditView):
    queryset = GeoJSONData.objects.all()
    model_form = GeoJSONDataForm
    template_name = "qgis_integration_plugin/edit_geojson_data.html"

    def get(self, request, pk):
        # Retrieve the GeoJSON data entry to be edited
        geojson_data = get_object_or_404(GeoJSONData, pk=pk)
        form = GeoJSONDataForm(instance=geojson_data)
        return render(request, self.template_name, {'form': form, 'geojson_data': geojson_data})

    def post(self, request, pk):
        geojson_data = get_object_or_404(GeoJSONData, pk=pk)
        form = GeoJSONDataForm(request.POST, instance=geojson_data)

        if form.is_valid():
            try:
                # Try to save inside a transaction block to avoid race conditions
                with transaction.atomic():
                    # Update properties
                    updated_properties = {
                        "name": form.cleaned_data['name'],
                        "description": form.cleaned_data['description'],
                        "comments": form.cleaned_data['comments'],
                        "pairs": form.cleaned_data['pairs'],
                        "type": form.cleaned_data['type'],
                        # You can add any other fields as needed
                    }

                    # Update properties field even if it's not directly modified
                    geojson_data.properties = updated_properties

                    # Save the form with the updated properties
                    form.save()

                # Success message
                messages.success(request, "Data updated successfully!")
                return redirect('QGIS_Integration_Plugin:api_explorer')

            except ValidationError as e:
                # Handle any form validation errors
                messages.error(request, f"Error saving data: {str(e)}")
                return render(request, self.template_name, {'form': form, 'geojson_data': geojson_data})

# View for deleting a GeoJSON entry
class GeoJSONDataDeleteView(generic.ObjectDeleteView):
    queryset = GeoJSONData.objects.all()

    def post(self, request, pk):
        if request.POST.get('_method') == 'DELETE':
            data = get_object_or_404(GeoJSONData, pk=pk)
            data.delete()  # Delete the entry from the database
            messages.success(request, "Data deleted successfully!")
            return redirect('QGIS_Integration_Plugin:api_explorer')
        else:
            return redirect('QGIS_Integration_Plugin:api_explorer')

# View for the API explorer interface
class GeoJSONAPIExplorerView(View):
    queryset = GeoJSONData.objects.all()
    template_name = "qgis_integration_plugin/api_explorer.html"

    def get(self, request):
        # Retrieve all GeoJSON data and render the API explorer page
        geojson_data = GeoJSONData.objects.all()
        return render(request, self.template_name, {"geojson_data": geojson_data})