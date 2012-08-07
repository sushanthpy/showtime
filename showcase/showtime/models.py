#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""Model for showtime."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

from django.db import models
from django.contrib.auth.backends import User


class Genre(models.Model):
  name = models.CharField(max_length=255, verbose_name='Genre')
  
  def __unicode__(self):
    return self.name
    
    
class Movies(models.Model):
  """Movies table."""
  Language_Choice = (
    ('English', 'English'),
    ('Hindi', 'Hindi')
  )
  
  name = models.CharField(max_length=255, verbose_name='Movie Name')
  release_date = models.DateField('Movie Release Date')
  language = models.CharField(max_length=255, verbose_name='Language', choices=Language_Choice)
  genre = models.ForeignKey(Genre, db_column='city')
  cast = models.CharField(max_length=255, verbose_name='Cast and Crew')
  director = models.CharField(max_length=255, verbose_name='Director')
  length = models.CharField(max_length=255, verbose_name='Length')
  writer = models.CharField(max_length=255, verbose_name='Writer')
  photo  = models.ImageField(upload_to='static/images', null=True, blank=True)
  story_line = models.TextField()
  status = models.BooleanField(default=1)
  
  def __unicode__(self):
    return self.name

  def image(self):
      return '<img src="/%s"/>' % self.photo
  
  image.allow_tags = True
  image.short_description = 'Thumbnail'

    

class Cities(models.Model):
  """List of citites name."""
  name = models.CharField(max_length=255, verbose_name='cities')
 
  def __unicode__(self):
    return self.name 


class Theaters(models.Model):
  """Theater table to store theater information."""
  name = models.CharField(max_length=255, verbose_name='Theater')
  city = models.ForeignKey(Cities, db_column='city', related_name='City')
  phone_number = models.CharField(max_length=255, verbose_name='Phone')
  address = models.CharField(max_length=255, verbose_name='Address')

  def __unicode__(self):
    return self.name


class ShowTimes(models.Model):
  """Movie Show Times information table."""
  Screen_Choice = (
    ('Screen 1', 'Screen 1'),
    ('Screen 2', 'Screen 2'),
    ('Screen 3', 'Screen 3')
  )
  
  movie = models.ForeignKey(Movies, db_column='movie', related_name='City')
  theater = models.ForeignKey(Theaters, db_column='theater')
  start_time = models.TimeField()
  screen = models.CharField(
    max_length=255, verbose_name='Screen', choices=Screen_Choice)
  
  def __str__(self):
      return '%s' % self.theater
    
  
class TicketOrder(models.Model):
  movie_name = models.ForeignKey(Cities, db_column='moviename', related_name='Name')
  name = models.CharField(max_length=255, verbose_name='Name')
  email_id = models.CharField(max_length=255, verbose_name='Email')
  phone = models.CharField(max_length=255, verbose_name='phone')
  seat_numbers = models.CharField(max_length=255, verbose_name='Screen')
  show_time = models.DateTimeField('Date Time')
  
  class Meta:
      db_table = 'ticket_order' 
  
  
  
  
  
