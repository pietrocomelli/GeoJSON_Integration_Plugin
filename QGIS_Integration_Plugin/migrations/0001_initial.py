from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0191_module_bay_rebuild'),
        ('circuits', '0044_circuit_groups'),
    ]

    operations = [
        # Creazione del modello GeoJSONData con tutti i campi necessari
        migrations.CreateModel(
            name='GeoJSONData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('pairs', models.IntegerField()),
                ('geometry', models.JSONField()),
                ('properties', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('related_device', models.ForeignKey(
                    to='dcim.Device',
                    on_delete=django.db.models.deletion.SET_NULL,
                    null=True,
                    blank=True,
                    help_text='Dispositivo associato, se applicabile.'
                )),
                ('related_circuit', models.ForeignKey(
                    to='circuits.Circuit',
                    on_delete=django.db.models.deletion.SET_NULL,
                    null=True,
                    blank=True,
                    help_text='Circuito associato, se applicabile.'
                )),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(
                    blank=True,
                    null=True,
                    help_text='Descrizione del dato GeoJSON.'
                )),
                ('comments', models.TextField(
                    blank=True,
                    null=True,
                    help_text='Commenti aggiuntivi sui dati GeoJSON.'
                )),
                ('custom_field_data', models.JSONField(
                    blank=True,
                    null=True,
                    help_text='Dati personalizzati associati al GeoJSON.'
                )),
            ],
        ),
    ]
