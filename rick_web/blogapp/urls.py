from django.conf.urls import url

from . import views

urlpatterns = [
    # index page -> /
    # 
    url(r'^$', views.index, name='index'),

    # about -> /about/ 
    #
    url(r'^about/$', views.about, name='about'),

    # blogpost -> /blogpost/ 
    #
    url(r'^post/$', views.blogpost, name='blogpost'),

    # contact -> /contact/ 
    #
    url(r'^contact/$', views.contact, name='contact'),

    # contact_msg -> /contact_msg/ 
    #
    url(r'^contact_msg/$', views.contact_msg, name='contact_msg'),


    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]


