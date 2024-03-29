from django.contrib import admin

from .models import *

@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')

@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'building')

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'teacher', 'subject', 'time_start', 'time_end', 'room')

@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Signup)
class SignupsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'subject', 'location', 'vk_id')

@admin.register(EventType)
class EventTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('type', 'date_from', 'date_to', 'group')

@admin.register(Day)
class DaysAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GenericAnswer)
class GenericAnswersAdmin(admin.ModelAdmin):
    list_display = ('input', 'output')

@admin.register(SituationAnswer)
class SituationAnswersAdmin(admin.ModelAdmin):
    list_display = ('situation', 'output')

@admin.register(Command)
class CommandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
#admin.site.register(Teachers)
#admin.site.register(Locations)
#admin.site.register(Groups)