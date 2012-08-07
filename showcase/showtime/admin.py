#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""Administration for showtime."""

from django.contrib import admin
from showtime import models


class ShowTimeInline(admin.TabularInline):
    model = models.ShowTimes
    extra = 3


class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'release_date', 'language', 'genre', 'cast',
        'director', 'length', 'writer', 'story_line', 'image', 'status'
        )
    list_display_links = ('name',)
    list_editable = ('status',)
    list_filter = ('release_date', 'name', 'language')
    inlines = [ShowTimeInline]
    search_fields = ['name']


class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theater', 'start_time')


#register movies model to admin page
admin.site.register(models.Movies, MoviesAdmin)
admin.site.register(models.Theaters)
admin.site.register(models.Cities)
admin.site.register(models.ShowTimes, ShowTimeAdmin)
admin.site.register(models.Genre)



