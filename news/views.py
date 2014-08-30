from django.views.generic import ListView, DetailView
from .models import News, UserProfile
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse


class NewsListView(ListView):
    model = News
    queryset = News.with_votes.all()


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'user_detail.html'


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['bio']
    template_name_suffix = '_update'

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user})
