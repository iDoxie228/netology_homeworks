from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='measurements/', blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')

