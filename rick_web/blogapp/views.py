# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from blogapp.models import Post

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
        'posts': Post.objects.all()[:5]
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





# FIXME - post2
#
def post2(request):
    context = { }
    return render(request, 'blogapp/post2.html', context)



# FIXME
#
def view_post(request, slug):   
    context = {
        'post': get_object_or_404(Post, slug=slug)
    }
    return render(request, 'blogapp/post_template.html', context)














# contact - blog contact page
#
def contact(request):
    context = {
    }
    return render(request, 'blogapp/contact.html', context)


# contact message- processes the contact form input
#
def contact_msg(request):
    message = "Please use the contact form to email contact@rickyan.com."
    if request.is_ajax():
        if request.method == "POST":
            name  = request.POST['name']
            email = request.POST['email']
            msg   = request.POST['message']

            send_mail( 
                "[CONTACT FORM] - " + name,
                "You have received a new message from your website contact form.\n\nHere are the details:\n\nName: "
                +name+"\n\nEmail: "+email+"\n\nMessage:\n\n"+msg,
                settings.EMAIL_HOST_USER,
                ['contact@rickyan.com'],
            )

            # Mail is Sent
            #
            message = "Mail sent to contact@rickyan.com."

    context = {
        'message': message,
    }
    return render(request, 'blogapp/contact_msg.html', context)




