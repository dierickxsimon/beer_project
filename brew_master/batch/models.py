from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Batch(models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    orginal_gravity = models.FloatField(default=1.030, null=True, blank=True)
    excepted_gravity = models.FloatField(default=1.000, null=True, blank=True)
    final_gravity = models.FloatField(default=None, null=True, blank=True)
    abv = models.FloatField(default=0, blank=True, null=True, editable=False)
    is_selected = models.BooleanField(default=False)
    setting = models.OneToOneField('Setting', null=True, blank=True, on_delete=models.CASCADE)
    yeast = models.ForeignKey('Yeast', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)
    

    def __str__(self):
        return self.name
    
    class Meta:
         ordering = ['-created',]
        
    def save(self, *args, **kwargs):
        if self.is_selected:
            Batch.objects.exclude(pk=self.pk).update(is_selected=False)

        if self.final_gravity:
            gravity_post = self.final_gravity       
        else:
            gravity_post = self.excepted_gravity   
            
        self.abv = (487*(self.orginal_gravity - gravity_post))/(4.75 - gravity_post)


        super(Batch, self).save(*args, **kwargs)

class Setting(models.Model):
    set_T = models.FloatField(default=15)
    min_T = models.FloatField(default=14.5, editable=False)
    max_T = (models.FloatField(default=15.5, editable=False))
    T_interval = models.FloatField(default=1)
    callibrated_T = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)
    
    
    
    def save(self, *args, **kwargs):
        self.min_T = self.set_T - self.T_interval/2
        self.max_T = self.set_T + self.T_interval/2

        super(Setting, self).save(*args, **kwargs)


class Yeast(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    max_T = models.FloatField(default=20)
    min_T = models.FloatField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
            return self.name
     

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
            return self.name
