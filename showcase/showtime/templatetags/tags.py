#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""Custom template tags for showtime."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

from django import template

register = template.Library()


@register.filter
def hash(object, attr):
    """Template for hashing the values."""
    gen_context = {'object': object}
    try:
      value = template.Variable(
          'object.%s' %attr).resolve(gen_context)
    except template.VariableDoesNotExist:
      value = ' '
    return value          