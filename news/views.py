from django.views.generic import ListView, DetailView
from .models import News, UserProfile
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic.edit import (
    UpdateView,
    CreateView
)


class NewsListView(ListView):
    model = News
    queryset = News.with_votes.all()
    paginate_by = 5


class NewsDetailView(DetailView):
    model = News


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


class NewsLinkCreateView(CreateView):
    model = News
    fields = ['title', 'url']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super(NewsLinkCreateView, self).form_valid(form)
