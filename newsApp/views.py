from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from djangoWebApp import settings
from newsapi import NewsApiClient

api = NewsApiClient(api_key=settings.NEWS_API_KEY)

# Search news articles by some specific search term

def home(request):
    article_list = api.get_everything(q='health')
    errorStatus = False
    if article_list['status'] == 'error':
        errorStatus = True
    else:
        article_list = article_list['articles']
    is_paginated = True
    paginator = Paginator(article_list, 12)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    for article in articles:
        x = article['publishedAt']
        article['publishedAt'] = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%B %d %Y, %I:%M %p")

    return render(request, 'news/index.html', {'article_list':articles, 'status': errorStatus} )

def contact(request):
    return render(request, 'news/contact.html')
