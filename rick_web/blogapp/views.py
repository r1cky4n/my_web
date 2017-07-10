# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse



#=======================================================================================================================
# Views for Bootstrap blog template
# 
# FIXME - for now, using views to generate a static blog. Add parameters
#         to the views to make the views dynamically generate content
#=======================================================================================================================


# index - blog landing page
#
def index(request):
    test_value = False;
    context = {
        'test_value':   test_value,        
    }
    return render(request, 'blogapp/index.html', context)


# about - blog about page
#
def about(request):
    return HttpResponse("Hello, world. Blogapp about...")


# blogpost - generated blog post page FIXME: parameterize 
#
def blogpost(request):
    return HttpResponse("Hello, world. Blogapp blogpost...")


# contact - blog contact page
#
def contact(request):
    return HttpResponse("Hello, world. Blogapp contact...")





