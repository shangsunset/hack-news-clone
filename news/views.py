from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    model = News
    queryset = News.with_votes.all()
