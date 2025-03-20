from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from ipam.models import Prefix
from .models import GeoJSONData

# Form to create or update GeoJSONData objects
class GeoJSONDataForm(NetBoxModelForm):
    class Meta:
        model = GeoJSONData  # Specify the model for this form
        fields = ('name', 'type', 'description', 'comments', 'pairs', 'geometry', 'properties')  # Fields to be included in the form

# Form to filter GeoJSONData objects based on specified criteria
class GeoJSONDataFilterForm(NetBoxModelFilterSetForm):
    model = GeoJSONData  # Specify the model for this filter form
    name = forms.CharField(
        required=False  # Name field for searching GeoJSONData (optional)
    )
    type = forms.CharField(
        required=False  # Type field for filtering GeoJSONData (optional)
    )

# Form to upload a GeoJSON file
class GeoJSONUploadForm(forms.Form):
    geojson_file = forms.FileField(
        label='Carica file GeoJSON',  # Label for the file upload field
        required=True,  # The field is required
        help_text='Seleziona un file GeoJSON da caricare.'  # Help text to guide the user
    )

    # Validate that the uploaded file is a valid GeoJSON file
    def clean_geojson_file(self):
        file = self.cleaned_data.get('geojson_file')

        # Check if the file is a valid GeoJSON file (optional check)
        if file.content_type != 'application/geo+json':
            raise forms.ValidationError('Il file caricato non è un file GeoJSON valido.')  # Raise error if file is not GeoJSON

        return file
