# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
from django.dispatch.dispatcher import receiver

from sundial.fields import TimezoneField
from sundial.utils import set_session_timezone
from sundial.zones import COMMON_GROUPED_CHOICES

class User(AbstractUser):
    timezone = TimezoneField(
        default='Etc/GMT-5', choices=COMMON_GROUPED_CHOICES
    )
    class Meta:
        managed = True

@receiver(user_logged_in)
def assign_user_timezone(request, user, **kwargs):
    set_session_timezone(request.session, user.timezone)

class Group(models.Model):
    location = models.ForeignKey(
        'Location',
        verbose_name='локация',
        on_delete=models.CASCADE,
        default=None
    )
    time_start = models.TimeField(verbose_name='время начала')
    time_end = models.TimeField(verbose_name='время конца')
    days = models.ManyToManyField(
        'Day',
        verbose_name='дни',
        blank=True, null=True
    )
    teacher = models.ForeignKey(
        'Teacher',
        verbose_name='учитель',
        on_delete=models.CASCADE,
        default=None
    )
    name = models.CharField(verbose_name='название', max_length=50)
    description = models.CharField(verbose_name='описание', max_length=255, blank=True, null=True)
    subject = models.ForeignKey(
        'Subject',
        verbose_name='предмет',
        on_delete=models.CASCADE,
        default=None
    )

    class Meta:
        #managed = False
        db_table = 'groups'
        verbose_name = 'группу'
        verbose_name_plural = 'группы'
    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(verbose_name='страна', max_length=50)
    region = models.CharField(verbose_name='регион', max_length=50)
    city = models.CharField(verbose_name='город', max_length=50)
    street = models.CharField(verbose_name='улица', max_length=50)
    building = models.CharField(verbose_name='здание', max_length=50)
    name = models.CharField(verbose_name='название', max_length=50)
    latitude = models.FloatField(verbose_name='широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name='долгота', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'locations'
        verbose_name = 'локацию'
        verbose_name_plural = 'локации'
    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    first_name = models.CharField(verbose_name='имя', max_length=50)
    middle_name = models.CharField(verbose_name='отчество', max_length=50)
    phone = models.CharField(verbose_name='телефон', max_length=20, blank=True, null=True)
    mail = models.CharField(verbose_name='почта', max_length=50, blank=True, null=True)
    age = models.IntegerField(verbose_name='возраст', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'teachers'
        verbose_name = 'учителя'
        verbose_name_plural = 'учителя'
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Subject(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    description = models.TextField(verbose_name='описание')
    class Meta:
        #managed = False
        db_table = 'subjects'
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
    def __str__(self):
        return self.name


class Signup(models.Model):
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    first_name = models.CharField(verbose_name='имя', max_length=50)
    middle_name = models.CharField(verbose_name='отчество', max_length=50)
    vk_id = models.IntegerField(verbose_name='vk id',)
    subject = models.ForeignKey(
        'Subject',
        verbose_name='предмет',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    location = models.ForeignKey(
        'Location',
        verbose_name='локация',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    notes = models.TextField(verbose_name='примечания')
    class Meta:
        #managed = False
        db_table = 'signups'
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
    def __str__(self):
        return self.last_name + ' ' + self.first_name


class EventType(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    class Meta:
        #managed = False
        db_table = 'event_types'
        verbose_name = 'тип события'
        verbose_name_plural = 'типы событий'
    def __str__(self):
        return self.name


class Event(models.Model):
    type = models.ForeignKey(
        'EventType',
        verbose_name='тип',
        on_delete=models.CASCADE,
        default=1
    )
    description = models.TextField(verbose_name='описание', blank=True)
    date_from = models.DateTimeField(verbose_name='дата с')
    date_to = models.DateTimeField(verbose_name='дата на')
    group = models.ForeignKey(
        'Group',
        verbose_name='группа',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    class Meta:
        #managed = False
        db_table = 'events'
        verbose_name = 'событие'
        verbose_name_plural = 'события'
    def __str__(self):
        return str(self.type) + ' ' + str(self.group)


class Day(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    class Meta:
        #managed = False
        ordering = ('id',)
        db_table = 'daysofweek'
        verbose_name = 'день недели'
        verbose_name_plural = 'дни недели'
    def __str__(self):
        return self.name


class GenericAnswer(models.Model):
    input = models.CharField(verbose_name='ввод', max_length=50)
    output = models.TextField(verbose_name='вывод')
    class Meta:
        #managed = False
        db_table = 'genericanswers'
        verbose_name = 'обычный ответ'
        verbose_name_plural = 'обычные ответы'
    def __str__(self):
        return self.input


class SituationAnswer(models.Model):
    situation = models.CharField(verbose_name='ситуация', max_length=50)
    output = models.TextField(verbose_name='вывод',)
    class Meta:
        #managed = False
        db_table = 'situationanswers'
        verbose_name = 'ситуационный ответ'
        verbose_name_plural = 'ситуационные ответы'
    def __str__(self):
        return self.situation

class Command(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    description = models.TextField(verbose_name='описание')
    no_argument_response = models.CharField(verbose_name='ответ когда нету аргумента', max_length=100)
    not_found_response = models.CharField(verbose_name='ответ когда не найдено', max_length=100)
    class Meta:
        #managed = False
        db_table = 'commands'
        verbose_name = 'комманду'
        verbose_name_plural = 'комманды'
    def __str__(self):
        return self.name
