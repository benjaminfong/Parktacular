# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DboSfmtaManagedOffstreetParking20240328(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_name = models.CharField(db_column='FACILITY_NAME', max_length=100)  # Field name made lowercase.
    street_address = models.CharField(db_column='STREET_ADDRESS', max_length=100)  # Field name made lowercase.
    main_entrance_long = models.FloatField(db_column='MAIN_ENTRANCE_LONG')  # Field name made lowercase.
    main_entrance_lat = models.FloatField(db_column='MAIN_ENTRANCE_LAT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo.sfmta_managed_offstreet_parking_20240328'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SfmtaManagedOffstreetParking20240328(models.Model):
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    osp_id = models.IntegerField(db_column='OSP_ID', blank=True, null=True)  # Field name made lowercase.
    facility_name = models.TextField(db_column='FACILITY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    street_address = models.TextField(db_column='STREET_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location = models.TextField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pm_district_id = models.IntegerField(db_column='PM_DISTRICT_ID', blank=True, null=True)  # Field name made lowercase.
    area_type = models.TextField(db_column='AREA_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blockface_id = models.IntegerField(db_column='BLOCKFACE_ID', blank=True, null=True)  # Field name made lowercase.
    street_seg_ctrln_id = models.IntegerField(db_column='STREET_SEG_CTRLN_ID', blank=True, null=True)  # Field name made lowercase.
    facility_type = models.TextField(db_column='FACILITY_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    owner = models.TextField(db_column='OWNER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensor_flag = models.TextField(db_column='SENSOR_FLAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meter_flag = models.TextField(db_column='METER_FLAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_feed_flag = models.TextField(db_column='DATA_FEED_FLAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    services = models.TextField(db_column='SERVICES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    web_site = models.TextField(db_column='WEB_SITE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    veh_entry_lanes = models.IntegerField(db_column='VEH_ENTRY_LANES', blank=True, null=True)  # Field name made lowercase.
    mc_entry_lanes = models.IntegerField(db_column='MC_ENTRY_LANES', blank=True, null=True)  # Field name made lowercase.
    veh_exit_lanes = models.IntegerField(db_column='VEH_EXIT_LANES', blank=True, null=True)  # Field name made lowercase.
    mc_exit_lanes = models.IntegerField(db_column='MC_EXIT_LANES', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='SYSTEM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hi_vol_disc_flag = models.TextField(db_column='HI_VOL_DISC_FLAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    validation_pgm = models.TextField(db_column='VALIDATION_PGM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sp_evt_rates = models.TextField(db_column='SP_EVT_RATES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activation_fee = models.IntegerField(db_column='ACTIVATION_FEE', blank=True, null=True)  # Field name made lowercase.
    card_replace_fee = models.IntegerField(db_column='CARD_REPLACE_FEE', blank=True, null=True)  # Field name made lowercase.
    late_fee = models.IntegerField(db_column='LATE_FEE', blank=True, null=True)  # Field name made lowercase.
    reopen_fee = models.IntegerField(db_column='REOPEN_FEE', blank=True, null=True)  # Field name made lowercase.
    no_key_valet_fee = models.IntegerField(db_column='NO_KEY_VALET_FEE', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='CAPACITY', blank=True, null=True)  # Field name made lowercase.
    main_entrance_long = models.DecimalField(db_column='MAIN_ENTRANCE_LONG', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    main_entrance_lat = models.DecimalField(db_column='MAIN_ENTRANCE_LAT', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    created_dt = models.TextField(db_column='CREATED_DT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_upd_dt = models.TextField(db_column='LAST_UPD_DT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    globalid = models.TextField(db_column='GLOBALID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shape = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_as_of = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_loaded_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    analysis_neighborhood = models.TextField(blank=True, null=True)  # This field type is a guess.
    supervisor_district = models.IntegerField(blank=True, null=True)
    analysis_neighborhoods = models.IntegerField(blank=True, null=True)
    neighborhoods = models.IntegerField(blank=True, null=True)
    sf_find_neighborhoods = models.IntegerField(db_column='SF_find_neighborhoods', blank=True, null=True)  # Field name made lowercase.
    current_police_districts = models.IntegerField(blank=True, null=True)
    current_supervisor_districts = models.IntegerField(blank=True, null=True)
    price_per_hour = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    close_hours = models.TimeField(blank=True, null=True)
    open_hours = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfmta_managed_offstreet_parking_20240328'
