# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import ugettext as _


class Group(models.Model):
    location = models.ForeignKey(
        'Location',
        verbose_name=_('location'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    time_start = models.TimeField(verbose_name=_('time start'))
    time_end = models.TimeField(verbose_name=_('time end'))
    days = models.ManyToManyField(
        'Day',
        verbose_name=_('days'),
        blank=True, null=True
    )
    teacher = models.ForeignKey(
        'Teacher',
        verbose_name=_('teacher'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    name = models.CharField(verbose_name=_('name'), max_length=50)
    description = models.CharField(verbose_name=_('description'), max_length=255, blank=True)
    subject = models.ForeignKey(
        'Subject',
        verbose_name=_('subject'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    class Meta:
        #managed = False
        db_table = 'groups'
        verbose_name = _('group')
        verbose_name_plural = _('groups')
    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(verbose_name=_('country'), max_length=50)
    region = models.CharField(verbose_name=_('region'), max_length=50)
    city = models.CharField(verbose_name=_('city'), max_length=50)
    street = models.CharField(verbose_name=_('street'), max_length=50)
    building = models.CharField(verbose_name=_('building'), max_length=50)
    name = models.CharField(verbose_name=_('name'), max_length=50)
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))

    class Meta:
        #managed = False
        db_table = 'locations'
        verbose_name = _('location')
        verbose_name_plural = _('locations')
    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField(verbose_name=_('last name'), max_length=50)
    first_name = models.CharField(verbose_name=_('first name'), max_length=50)
    middle_name = models.CharField(verbose_name=_('middle name'), max_length=50)
    phone = models.CharField(verbose_name=_('phone'), max_length=20)
    mail = models.CharField(verbose_name=_('mail'), max_length=50)
    age = models.IntegerField(verbose_name=_('age'))

    class Meta:
        #managed = False
        db_table = 'teachers'
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Subject(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    description = models.TextField(verbose_name=_('description'))
    class Meta:
        #managed = False
        db_table = 'subjects'
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')
    def __str__(self):
        return self.name


class Signup(models.Model):
    last_name = models.CharField(verbose_name=_('last name'), max_length=50)
    first_name = models.CharField(verbose_name=_('first name'), max_length=50)
    middle_name = models.CharField(verbose_name=_('middle name'), max_length=50)
    vk_id = models.IntegerField(verbose_name=_('vk id'),)
    subject = models.ForeignKey(
        'Subject',
        verbose_name=_('subject'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    location = models.ForeignKey(
        'Location',
        verbose_name=_('location'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    notes = models.TextField(verbose_name=_('notes'))
    class Meta:
        #managed = False
        db_table = 'signups'
        verbose_name = _('signup')
        verbose_name_plural = _('signups')
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class EventType(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    class Meta:
        #managed = False
        db_table = 'event_types'
        verbose_name = _('event type')
        verbose_name_plural = _('event types')
    def __str__(self):
        return self.name


class Event(models.Model):
    type = models.ForeignKey(
        'EventType',
        verbose_name=_('type'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    description = models.TextField(verbose_name=_('description'), blank=True)
    date_from = models.DateField(verbose_name=_('date from'))
    date_to = models.DateField(verbose_name=_('date to'))
    group = models.ForeignKey(
        'Group',
        verbose_name=_('group'),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    class Meta:
        #managed = False
        db_table = 'events'
        verbose_name = _('event')
        verbose_name_plural = _('events')
    def __str__(self):
        return str(self.type) + ' ' + str(self.group)


class Day(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    class Meta:
        #managed = False
        ordering = ('id',)
        db_table = 'daysofweek'
        verbose_name = _('day of week')
        verbose_name_plural = _('days of week')
    def __str__(self):
        return self.name


class GenericAnswer(models.Model):
    input = models.CharField(verbose_name=_('input'), max_length=50)
    output = models.TextField(verbose_name=_('output'))
    class Meta:
        #managed = False
        db_table = 'genericanswers'
        verbose_name = _('generic answer')
        verbose_name_plural = _('generic answers')
    def __str__(self):
        return self.input


class SituationAnswer(models.Model):
    situation = models.CharField(verbose_name=_('situation'), max_length=50)
    output = models.TextField(verbose_name=_('output'),)
    class Meta:
        #managed = False
        db_table = 'situationanswers'
        verbose_name = _('situation answer')
        verbose_name_plural = _('situation answers')
    def __str__(self):
        return self.situation

class Command(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    description = models.TextField(verbose_name=_('description'))
    no_argument_response = models.CharField(verbose_name=_('no argument response'), max_length=100)
    not_found_response = models.CharField(verbose_name=_('not found response'), max_length=100)
    class Meta:
        #managed = False
        db_table = 'commands'
        verbose_name = _('command')
        verbose_name_plural = _('commands')
    def __str__(self):
        return self.name
