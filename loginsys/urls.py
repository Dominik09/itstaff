from  django.conf.urls import patterns, include, url

urlpatterns = patterns('loginsys.views',
    url(r'^login/', 'login'),
    url(r'^logout/', 'logout'),
    url(r'^registration/', 'register'),
 	url(r'^profile/(?P<Uid>\d+)/$', 'my_profile', name = 'Profile'),
    )

urlpatterns += patterns('',
    url(r'^', 'loginsys.views.main_page'),
)