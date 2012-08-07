#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""form for showtime."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

from django import forms
from showtime import models

choice_location = (
    ('Hyderabad', 'Hyd'),
)

class SearchForm(forms.Form):
    """Search form for showtime."""
    Location = forms.ChoiceField(choices=choice_location)
    movies = forms.ModelChoiceField(
        queryset=models.Movies.objects.filter(status='1'))
    date = forms.DateTimeField()  
      

