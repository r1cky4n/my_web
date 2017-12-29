from django.conf.urls import url

from . import views

urlpatterns = [
    # index page -> /
    # 
    url(r'^$', views.index, name='index'),

    # about -> /about/ 
    #
    url(r'^about/$', views.about, name='about'),

    # DB Stored Blog Post -> /post/...
    #
    url(r'^post/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),

    # contact -> /contact/ 
    #
    url(r'^contact/$', views.contact, name='contact'),

    # contact_msg -> /contact_msg/ 
    #
    url(r'^contact_msg/$', views.contact_msg, name='contact_msg'),

]


