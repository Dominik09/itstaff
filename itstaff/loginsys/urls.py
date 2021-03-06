from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^registration/', 'loginsys.views.registration'),
    url(r'^profile/(?P<Uid>\d+)/$', 'loginsys.views.get_profile'),
    url(r'^', 'loginsys.views.main_page'),
)
