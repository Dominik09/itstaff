from django.conf.urls import include, url
from django.contrib import admin
import sheet

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('loginsys.urls')),
    
   	url(r'^', include('sheet.urls')),
	url(r'^$', 'ittracker.views.main_page'),
	url(r'^test/$', 'loginsys.views.test', name='Test'),
	url(r'^', include('loginsys.urls')),
	]
