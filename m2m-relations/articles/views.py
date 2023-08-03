from django.shortcuts import render
from articles.models import Article


def articles_list(request):

    object_list = Article.objects.all()
    context = {
        'object_list': object_list,
    }

    template = 'articles/news.html'
    return render(request, template, context)









