#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""urls for showcase."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

import os

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

PROJECT_PATH = os.path.dirname(__file__)

urlpatterns = patterns('',
    url(r'^$', 'showtime.views.ShowMovies', name='home'),
    url(r'^book/(?P<movie_id>\d+)/$', 'showtime.views.BookTickets', name='tickets'),
    url(r'^checkout/$', 'showtime.views.CheckOut', name='checkout'),
    url(r'^data/$', 'showtime.views.Data', name='data'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PROJECT_PATH, 'static')}),                  
)
