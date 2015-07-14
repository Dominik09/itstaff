from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^articles/get/(?P<art_id>\d+)/$', 'article.views.single_article'),
    url(r'^like/(?P<art_id>\d+)/$', 'article.views.like'),
    url(r'^back/', 'article.views.backto'),
    url(r'^temp/', 'article.views.template'),
    url(r'^articles/addcomment/(?P<art_id>\d+)/$', 'article.views.addcomment'),
    url(r'^', 'article.views.all_article'),
)