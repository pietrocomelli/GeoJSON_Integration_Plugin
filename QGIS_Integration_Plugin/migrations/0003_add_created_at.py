from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("QGIS_Integration_Plugin", "0002_add_properties"),
    ]

    operations = [
        migrations.AddField(
            model_name="geojsondata",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
