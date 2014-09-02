from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News, UserProfile, Vote
from .forms import VoteForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView,
    FormView
)
from django.core.urlresolvers import reverse, reverse_lazy


class NewsListView(ListView):
    model = News
    queryset = News.with_votes.all()
    paginate_by = 5


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


class NewsDetailView(DetailView):
    model = News


class NewsLinkUpdateView(UpdateView):
    model = News
    fields = ['title', 'url']


class NewsLinkDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('home')


class VoteFormView(FormView):
    model = Vote
    form_class = VoteForm

    def form_valid(self, form):
        news = get_object_or_404(News, pk=form.data['news'])
        user = self.request.user
        votes = Vote.objects.filter(voter=user, news=news)
        has_voted = (votes.count() > 0)

        if not has_voted:
            Vote.objects.create(voter=user, news=news)
        else:
            votes[0].delete()

        return redirect('home')

    def form_invalid(self, form):
        return redirect('home')
