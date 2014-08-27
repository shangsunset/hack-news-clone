from django.contrib import admin
from .models import News, Vote


class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)


class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)
