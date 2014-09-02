from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from news.views import (
    NewsListView,
    NewsDetailView,
    UserProfileDetailView,
    UserProfileUpdateView,
    NewsLinkCreateView,
    NewsLinkUpdateView,
    NewsLinkDeleteView,
    VoteFormView
)
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^$', NewsListView.as_view(), name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
        name='profile'),
    url(r'^update-profile/$', login_required(UserProfileUpdateView.as_view()),
        name='update_profile'),
    url(r'^news/create/$', login_required(NewsLinkCreateView.as_view()),
        name='news_create'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailView.as_view(),
        name='news_detail'),
    url(r"^news/update/(?P<pk>\d+)/$", login_required(
        NewsLinkUpdateView.as_view()),
        name="news_update"),
    url(r"^news/delete/(?P<pk>\d+)/$", login_required(
        NewsLinkDeleteView.as_view()),
        name="news_delete"),
    url(r'^vote/$', login_required(VoteFormView.as_view()),
        name='vote'),
)
