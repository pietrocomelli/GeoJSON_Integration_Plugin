from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("QGIS_Integration_Plugin", "0001_initial"),  # Assicurati che il nome dell'app sia corretto
    ]

    operations = [
        migrations.AddField(
            model_name="geojsondata",  # Sostituisci con il nome corretto del tuo modello
            name="properties",
            field=models.JSONField(default=dict),  # Puoi cambiare il tipo di campo se serve
        ),
    ]

