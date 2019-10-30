from django.contrib import admin

from .models import *

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname')

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_start', 'time_end', 'days')

#admin.site.register(Teachers)
#admin.site.register(Locations)
#admin.site.register(Groups)