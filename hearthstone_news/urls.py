from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from news.views import (
    NewsListView,
    NewsDetailView,
    UserProfileDetailView,
    UserProfileUpdateView,
    NewsLinkCreateView
)
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', NewsListView.as_view(), name='home'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
        name='profile'),
    url(r'^update-profile/$', login_required(UserProfileUpdateView.as_view()),
        name='update_profile'),
    url(r'^news/create/$', login_required(NewsLinkCreateView.as_view()),
        name='news_create'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailView.as_view(),
        name='news_detail'),
)
