from django.db import models
from batch.models import Batch
import uuid

# Create your models here.
class Data(models.Model):
    set_temprature = models.FloatField(null=True, blank=True)
    temprature = models.FloatField()
    fridge = models.BooleanField(default=False)
    warm_element = models.BooleanField(default=False)
    batch = models.ForeignKey(Batch, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    class meta:
        ordering = ['-created']

    def __str__(self):
        date = self.created.strftime('%Y-%m-%d %H:%M:%S')
        return date
