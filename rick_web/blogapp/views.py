# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blogapp.forms import ContactForm


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

    contact_form = ContactForm

    context = {
        'contact_form': contact_form    
    }
    return render(request, 'blogapp/contact.html', context)


# contact message- processes the contact form input
#
def contact_msg(request):
    if request.is_ajax():
        if request.method == "POST":
            name = request.POST['name']

        message = "Yes, AJAX!"
    else:
        message = "Please use the contact form to email contact@rickyan.com."
    return HttpResponse(message)




