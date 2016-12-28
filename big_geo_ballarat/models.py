from __future__ import unicode_literals

from django.db import models


# Create your models here.
class data_crs(models.Model):
    crs_type = models.CharField(default="name", max_length=4)
    crs_properties_name = models.CharField(max_length=50)

    def __str__(self):
        return self.crs_properties_name


class data_geo(models.Model):
    geo_data_label = models.CharField(primary_key=True, max_length=50)
    geo_data_type = models.CharField(default="FeatureCollection", max_length=30)
    geo_data_table = models.CharField(default="Enter Table Reference Here", max_length=100)

    def __str__(self):
        return self.geo_data_label


class feature_geometry(models.Model):
    geometry_id = models.CharField(max_length=50)

    geometry_type = models.CharField(default="Point", max_length=10)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.FloatField()

    geometry_name = models.CharField(default="geom", max_length=4)
    central_as = models.IntegerField()
    site_name = models.CharField(max_length=200)
    feature_lo = models.CharField(max_length=200)
    feature_ty = models.CharField(max_length=200)
    centroid_e = models.FloatField()
    centroid_n = models.FloatField()

    feature_data_geo = models.ForeignKey(data_geo, null=False)
    feature_data_crs = models.ForeignKey(data_crs, blank=True)

    def __str__(self):
        return self.site_name
