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
        #'test_value':   test_value,        
    }
    return render(request, 'blogapp/index.html', context)


# about - blog about page
#
def about(request):
    context = { }
    return render(request, 'blogapp/about.html', context)


# blogpost - generated blog post page FIXME: parameterize 
#
def blogpost(request):
    context = { }
    return render(request, 'blogapp/post.html', context)


# contact - blog contact page
#
def contact(request):
    context = { }
    return render(request, 'blogapp/contact.html', context)





