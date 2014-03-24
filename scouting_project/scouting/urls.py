from django.conf.urls import patterns, url

from scouting import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    #adding url for teamdata_list page
    url(r'^teamdata_list/$', views.teamdata_list, name='teamdata_list'),


)
