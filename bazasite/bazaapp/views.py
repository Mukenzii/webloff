from django.shortcuts import render
from  django.views.generic import ListView
from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        'categories': categories,
        'articles': articles,
        'title': "Dizayn-Baza"
    }


    return render(request, 'bazaapp/index.html',context)


