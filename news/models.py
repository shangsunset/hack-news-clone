from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User


class NewsVoteManager(models.Manager):
    def get_queryset(self):
        return super(NewsVoteManager, self) \
            .get_queryset() \
            .annotate(votes=Count('vote')) \
            .order_by('-votes')


class News(models.Model):
    title = models.CharField('Headline', max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User)
    ranking = models.FloatField(default=0.0)
    content = models.TextField(blank=True)
    url = models.URLField('URL', max_length=250, blank=True)

    objects = models.Manager()
    with_votes = NewsVoteManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Vote(models.Model):
    voter = models.ForeignKey(User)
    news = models.ForeignKey(News)

    def __unicode__(self):
        return '%s voted for %s' % (self.voter.username, self.news.title)

    class Meta:
        verbose_name = 'Vote'
