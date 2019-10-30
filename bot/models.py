# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Groups(models.Model):
    location = models.ForeignKey(
        'Locations',
        on_delete=models.CASCADE,
        default=None,
        blank=True, null=True
    )
    time_start = models.TimeField()
    time_end = models.TimeField()
    days = models.CharField(max_length=14)
    teacher = models.ForeignKey(
        'Teachers',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    class Meta:
        #managed = False
        db_table = 'groups'
    def __str__(self):
        return self.name


class Locations(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        #managed = False
        db_table = 'locations'
    def __str__(self):
        return self.name


class Teachers(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'teachers'
    def __str__(self):
        return self.lastname + ' ' + self.firstname