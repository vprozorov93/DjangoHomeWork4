from django.shortcuts import render

from articles.models import Article, ArticleTag


def articles_list(request):
    template = 'articles/news.html'
    news = Article.objects.prefetch_related('scopes', 'scopes__tag').order_by('-published_at')

    context = {'object_list': news}

    return render(request, template, context)
