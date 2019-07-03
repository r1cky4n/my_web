"""Views."""
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from blogapp.models import Post


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    """Index page."""
    context = {
        'posts': reversed(Post.objects.all()[:5])
    }
    return render(request, 'blogapp/index.html', context)

def about(request):
    """About page."""
    context = {}
    return render(request, 'blogapp/about.html', context)

def view_post(request, slug):
    """Generate post page from database."""
    context = {
        'post': get_object_or_404(Post, slug=slug)
    }
    return render(request, 'blogapp/post_template.html', context)

def contact(request):
    """Contact page."""
    context = {
    }
    return render(request, 'blogapp/contact.html', context)

def contact_msg(request):
    """Contact Message - processes the contact form input."""
    message = "Please use the contact form to email contact@rickyan.com."
    if request.is_ajax():
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            msg = request.POST['message']

            # Mail is Sent
            #
            message = "Mail sent to contact@rickyan.com."

            send_mail(
                "[CONTACT FORM] - " + name,
                "You have received a new message from your website contact form."
                "\n\nHere are the details:\n\nName: "
                +name+"\n\nEmail: "+email+"\n\nMessage:\n\n"+msg,
                settings.EMAIL_HOST_USER,
                ['contact@rickyan.com'],
            )

    context = {
        'message': message,
    }
    return render(request, 'blogapp/contact_msg.html', context)
