from django.db import models

class GeoJSONData(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    pairs = models.IntegerField()
    geometry = models.JSONField()  # Per salvare la geometria (coordinate, tipo geometria, ecc.)
    properties = models.JSONField()  # Per salvare le proprietà associate alla geometria
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


