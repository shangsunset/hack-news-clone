from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import NewsListView
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'$', NewsListView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
