from django.contrib import admin

from .models import data_crs, data_geo, feature_geometry

# Register your models here.
admin.site.register(data_crs)
admin.site.register(data_geo)
admin.site.register(feature_geometry)