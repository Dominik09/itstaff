from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('sheet.views',
    url(r'^sheets/all/$', 'sheets'),
    url(r'^sheets/get/(?P<sheet_id>\d+)/$', 'sheet', name = 'Get_news'),
    url(r'^sheets/edit/(?P<sheet_id>\d+)/$', 'ednews', name='Edit_news'),

    url(r'^sheets/addlike/(?P<sheet_id>\d+)/$', 'addlike'),
    url(r'^sheets/addcomment/(?P<sheet_id>\d+)/$', 'addcomment'),
    url(r'^addnews/', 'addnews'),
    url(r'^list_news/', 'news_all', name='List_news'),

    )

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()