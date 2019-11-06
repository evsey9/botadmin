from django.contrib import admin

from .models import *

@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'subject', 'time_start', 'time_end', 'days')

@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Signup)
class SignupsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'subject', 'location')

@admin.register(EventType)
class EventTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('type', 'date_from', 'date_to', 'group')
#admin.site.register(Teachers)
#admin.site.register(Locations)
#admin.site.register(Groups)