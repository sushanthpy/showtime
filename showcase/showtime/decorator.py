#!/usr/bin/python2.7
#
# self @ 2012 , copyright reserved
"""views for showtime."""

__author__ = 'sushanth53@gmail.com (sushanth reddy)'

from django import shortcuts

def Render(template):
    """
    Decorator for Django views that sends returned dict to 
    render_to_response function with given template and
    RequestContext as context instance.

    Args:
     template: template name to use
    Returns:
     renders output to html
    
    Example Usage:
        @Render('index.html)
        def Test(request)
            text = "Hello World"
            return {'text': text} 
     
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return shortcuts.render_to_response(
                    output[1], output[0], shortcuts.RequestContext(request))
            elif isinstance(output, dict):
                return shortcuts.render_to_response(
                  template, output, shortcuts.RequestContext(request))
            return output
        return wrapper
    return renderer