from django.conf.urls import patterns, include, url

from django.contrib import admin
#import scouting

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scouting_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^scouting/', include('scouting.urls')),
)
