# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DwDowjParamSrList(models.Model):
    id = models.FloatField(primary_key=True)
    sr_code = models.CharField(max_length=20, blank=True, null=True)
    sr_name = models.CharField(max_length=255, blank=True, null=True)
    sr_status = models.CharField(max_length=20, blank=True, null=True)
    sr_desc2_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_dowj_param_sr_list'


class DwDowjPersonProfileDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    profile_notes = models.CharField(max_length=4000, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_PROFILE_DTL'


class DwDowjPersonRoleDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    roletype = models.CharField(max_length=255, blank=True, null=True)
    occ_cat = models.CharField(max_length=20, blank=True, null=True)
    since_day = models.CharField(max_length=20, blank=True, null=True)
    since_month = models.CharField(max_length=20, blank=True, null=True)
    since_year = models.CharField(max_length=20, blank=True, null=True)
    to_day = models.CharField(max_length=20, blank=True, null=True)
    to_month = models.CharField(max_length=20, blank=True, null=True)
    to_year = models.CharField(max_length=20, blank=True, null=True)
    occ_title = models.CharField(max_length=500, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_ROLE_DTL'


class DwDowjPersonNameDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    name_type = models.CharField(max_length=255, blank=True, null=True)
    title_honorific = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    sur_name = models.CharField(max_length=255, blank=True, null=True)
    maiden_name = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    original_script_name = models.CharField(max_length=500, blank=True, null=True)
    single_string_name = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_NAME_DTL'


class DwDowjPersonDescDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    description3 = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_DESC_DTL'


class DwDowjPersonDateDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    date_type = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    dnotes = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_DATE_DTL'


class DwDowjPersonPlaceDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_PLACE_DTL'


class DwDowjPersonCntryDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    country_type = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_CNTRY_DTL'


class DwDowjPersonDocumentDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    id_notes = models.CharField(max_length=4000, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_DOCUMENT_DTL'


class DwDowjEntityDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(primary_key=True, max_length=20)
    action = models.CharField(max_length=20, blank=True, null=True)
    action_date = models.CharField(max_length=20, blank=True, null=True)
    active_status = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_DTL'


class DwDowjEntityDescDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.CharField(max_length=20, blank=True, null=True)
    description2 = models.CharField(max_length=20, blank=True, null=True)
    description3 = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_DESC_DTL'


class DwDowjEntityDateDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    date_type = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    dnotes = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_DATE_DTL'


class DwDowjEntityRefDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    since_day = models.CharField(max_length=20, blank=True, null=True)
    since_month = models.CharField(max_length=20, blank=True, null=True)
    since_year = models.CharField(max_length=20, blank=True, null=True)
    to_day = models.CharField(max_length=20, blank=True, null=True)
    to_month = models.CharField(max_length=20, blank=True, null=True)
    to_year = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_REF_DTL'


class DwDowjEntityCompanyDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    addr_line = models.CharField(max_length=255, blank=True, null=True)
    addr_city = models.CharField(max_length=255, blank=True, null=True)
    addr_cntry = models.CharField(max_length=255, blank=True, null=True)
    addr_url = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_COMPANY_DTL'


class DwDowjEntityCountryDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    country_type = models.CharField(max_length=255, blank=True, null=True)
    country_value = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_COUNTRY_DTL'


class DwDowjEntityDocumentDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    id_notes = models.CharField(max_length=4000, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_DOCUMENT_DTL'


class DwDowjEntityProfileDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    profile_notes = models.CharField(max_length=4000, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_PROFILE_DTL'


class DwDowjEntitySourceDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_SOURCE_DTL'


class DwDowjPersonDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(primary_key=True, max_length=20)
    action = models.CharField(max_length=20, blank=True, null=True)
    action_date = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    active_status = models.CharField(max_length=20, blank=True, null=True)
    deceased = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_DTL'


class DwDowjEntityNameDtl(models.Model):
    file_name = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=400, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    name_type = models.CharField(max_length=255, blank=True, null=True)
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    original_script_name1 = models.CharField(max_length=500, blank=True, null=True)
    original_script_name2 = models.CharField(max_length=255, blank=True, null=True)
    single_string_name = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_NAME_DTL'


class DwDowjRecordIndex(models.Model):
    record_name = models.CharField(max_length=500, blank=True, null=True)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    record_id = models.CharField(max_length=20, blank=True, null=True)
    id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_RECORD_INDEX'


class DwDowjPersonImageDtl(models.Model):
    id = models.FloatField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.CharField(max_length=20, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_PERSON_IMAGE_DTL'


class DwDowjAssociationsDtl(models.Model):
    id = models.FloatField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    record_id = models.CharField(max_length=20, blank=True, null=True)
    associate_type = models.CharField(max_length=20, blank=True, null=True)
    associate_id = models.CharField(max_length=20, blank=True, null=True)
    associate_code = models.CharField(max_length=255, blank=True, null=True)
    associate_ex = models.CharField(max_length=3, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ASSOCIATIONS_DTL'


class DwDowjAuditLog(models.Model):
    user_id = models.TextField(max_length=20)
    username = models.TextField(max_length=50)
    oper_type = models.TextField(max_length=50)
    oper_time = models.DateTimeField(default=timezone.now)
    oper_memo = models.TextField(max_length=400)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_AUTIT_LOG'


class DwDowjEntitySrDtl(models.Model):
    id = models.FloatField(primary_key=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    since_day = models.CharField(max_length=20, blank=True, null=True)
    since_month = models.CharField(max_length=20, blank=True, null=True)
    since_year = models.CharField(max_length=20, blank=True, null=True)
    to_day = models.CharField(max_length=20, blank=True, null=True)
    to_month = models.CharField(max_length=20, blank=True, null=True)
    to_year = models.CharField(max_length=20, blank=True, null=True)
    edw_data_dt = models.DateField(blank=True, null=True)
    sr_name = models.CharField(max_length=255, blank=True, null=True)
    sr_status = models.CharField(max_length=20, blank=True, null=True)
    sr_desc2_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DW_DOWJ_ENTITY_SR_DTL'
