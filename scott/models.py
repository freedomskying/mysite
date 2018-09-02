from django.db import models


# Create your models here.
class Bonus(models.Model):
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'scott'
        managed = False
        db_table = 'bonus'


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14, blank=True, null=True)
    loc = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        app_label = 'scott'
        managed = False
        db_table = 'dept'


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    mgr = models.IntegerField(blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='deptno', blank=True, null=True)

    class Meta:
        app_label = 'scott'
        managed = False
        db_table = 'emp'


class Salgrade(models.Model):
    grade = models.FloatField(blank=True, null=True)
    losal = models.FloatField(blank=True, null=True)
    hisal = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'scott'
        managed = False
        db_table = 'salgrade'
