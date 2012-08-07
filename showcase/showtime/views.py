#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""views for showtime."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

import collections
import re
import simplejson

from django import http
from django.views.decorators.csrf import csrf_exempt

from showtime import models
from showtime import decorator
from showtime import forms 


@decorator.Render('showtime/index.html')
def ShowMovies(request):
    """View to get the movies information.
    
    Args:
     request: HttpRequest
    
    Returns:
     {data}
    """
    get_movie_data = models.Movies.objects.filter(status='1')
    return {'data': get_movie_data}


@decorator.Render('showtime/book.html')
def BookTickets(request, movie_id=None):
    """View for booking tickets.
    
    Args:
     request: HttpRequest
     
    Returns:
     {data}
    """
    results = collections.defaultdict(dict)
    get_show_times = models.ShowTimes.objects.filter(movie=movie_id).values()
    
    get_move_name = models.Movies.objects.get(pk=movie_id)
    
    for fetch in get_show_times:
        theater = models.Theaters.objects.get(pk=fetch['theater_id'])
        screen = re.sub('\s', '', fetch['screen'])
        show_time = fetch['start_time']
        row = results[theater]
        row[screen] = show_time
    
    form = forms.SearchForm()
    screens = ['Screen1', 'Screen2', 'Screen3']
    return {'data': dict(results), 'screens': screens,
            'movie': get_move_name, 'form': form}



@decorator.Render('showtime/checkout.html')
def CheckOut(request):
    """View for booking tickets.
    
    Args:
     request: HttpRequest
     
    Returns:
     {data}
    """
    form = forms.OrderForm()
    return {'form': form}


@csrf_exempt
def Data(request):
    import logging
    if request.is_ajax():
       import simplejson
       data = request.raw_post_data
       data = data.replace('kk%5B%5D=', '')
       data =  data.replace('&', ',')
       obj = models.TicketOrder()
       return http.HttpResponse(data)
    else:
       return http.HttpResponse("Failed")
    