from django.contrib import admin
from .models import Batch,Tag, Setting, Yeast
# Register your models here.

admin.site.register(Batch)
admin.site.register(Tag)
admin.site.register(Setting)
admin.site.register(Yeast)

