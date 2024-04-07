from django.db import models
# from django.contrib.gis.db import models as geomodels
# from django.contrib.gis.geos import Point


# Create your models here.
class ParkingFacility(models.Model):
    ## get from models generated in inspection_result.py
    id = models.IntegerField(db_column='OBJECTID', primary_key=True)
    facility_name = models.TextField(db_column='FACILITY_NAME', blank=True, null=True)
    street_address = models.TextField(db_column='STREET_ADDRESS', blank=True, null=True)
    capacity = models.IntegerField(db_column='CAPACITY', blank=True, null=True)
    long = models.DecimalField(db_column='MAIN_ENTRANCE_LONG', max_digits=10, decimal_places=6,
                                             blank=True, null=True)
    lat = models.DecimalField(db_column='MAIN_ENTRANCE_LAT', max_digits=10, decimal_places=6, blank=True,
                                            null=True)
    price_per_hour = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    close_hours = models.TimeField(blank=True, null=True)
    open_hours = models.TimeField(blank=True, null=True)
    facility_type = models.TextField(db_column='FACILITY_TYPE', blank=True, null=True)
    owner = models.TextField(db_column='OWNER', blank=True, null=True)


    class Meta:
        # managed = False
        db_table = 'sfmta_managed_offstreet_parking_20240328'

