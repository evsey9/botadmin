# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Group(models.Model):
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    time_start = models.TimeField()
    time_end = models.TimeField()
    days = models.ManyToManyField(
        'Day',
        blank=True, null=True
    )
    teacher = models.ForeignKey(
        'Teacher',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    class Meta:
        #managed = False
        db_table = 'groups'
    def __str__(self):
        return self.name


class Location(models.Model):
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


class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'teachers'
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    class Meta:
        #managed = False
        db_table = 'subjects'
    def __str__(self):
        return self.name


class Signup(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    vk_id = models.IntegerField()
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    notes = models.TextField()
    class Meta:
        #managed = False
        db_table = 'signups'
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class EventType(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        #managed = False
        db_table = 'event_types'
    def __str__(self):
        return self.name


class Event(models.Model):
    type = models.ForeignKey(
        'EventType',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    description = models.TextField(blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    class Meta:
        #managed = False
        db_table = 'events'
    def __str__(self):
        return str(self.type) + ' ' + str(self.group)


class Day(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        #managed = False
        ordering = ('id',)
        db_table = 'daysofweek'
    def __str__(self):
        return self.name


class GenericAnswer(models.Model):
    input = models.CharField(max_length=50)
    output = models.TextField()
    class Meta:
        #managed = False
        db_table = 'genericanswers'


class Command(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    no_argument_response = models.CharField(max_length=100)
    not_found_response = models.CharField(max_length=100)
    class Meta:
        #managed = False
        db_table = 'commands'