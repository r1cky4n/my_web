from django.conf.urls import url

from . import views

urlpatterns = [
    # index page -> /
    # 
    url(r'^$', views.index, name='index'),

    # about -> /about/ 
    #
    url(r'^about/$', views.about, name='about'),

    # blogpost -> /post/ 
    #
    url(r'^post/$', views.blogpost, name='blogpost'),

    # FIXME - post 2 -> /post2/ 
    #
    url(r'^post2/$', views.post2, name='post2'),

    # contact -> /contact/ 
    #
    url(r'^contact/$', views.contact, name='contact'),

    # contact_msg -> /contact_msg/ 
    #
    url(r'^contact_msg/$', views.contact_msg, name='contact_msg'),







    # DB Stored Blog Post -> /post/...
    #
    url(r'^post/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),
    
    # DB Stored Blog Category -> /post/category/...
    url(r'^post/category/(?P<slug>[^\.]+)', views.view_category, name='view_blog_category'),
]


