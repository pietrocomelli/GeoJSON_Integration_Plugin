from django.db import migrations, models
import django.contrib.postgres.fields
import django.utils.timezone
import uuid

class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('dcim', '0191_module_bay_rebuild'),
    #     ('circuits', '0044_circuit_groups'),
    # ]


    operations = [
        migrations.CreateModel(
            name='GeoJSONData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=50)),
                ('pairs', models.IntegerField(null=True, blank=True)),
                ('geometry', models.JSONField()),
                ('properties', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('custom_field_data', models.JSONField(default=dict, blank=True, null=True)),
                # ('related_device', models.ForeignKey(
                #     on_delete=models.SET_NULL,
                #     to='dcim.Device',
                #     null=True, blank=True,
                #     related_name='geojson_data'
                # )),
                # ('related_circuit', models.ForeignKey(
                #     on_delete=models.SET_NULL,
                #     to='circuits.Circuit',
                #     null=True, blank=True,
                #     related_name='geojson_data'
                # )),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
