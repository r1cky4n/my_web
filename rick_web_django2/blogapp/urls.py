"""URLs."""
from django.urls import path, re_path

from . import views

urlpatterns = [
    # index page -> /
    #
    path('', views.index, name='index'),

    # about -> /about/
    #
    re_path(r'^about/$', views.about, name='about'),

    # DB Stored Blog Post -> /post/...
    #
    re_path(r'^post/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),

    # contact -> /contact/
    #
    re_path(r'^contact/$', views.contact, name='contact'),

    # contact_msg -> /contact_msg/
    #
    re_path(r'^contact_msg/$', views.contact_msg, name='contact_msg'),

]
