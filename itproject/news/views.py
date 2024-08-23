from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Artiles
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

def news(request):
    news = Artiles.objects.all()
    data = {
        'title': 'Новости на моём обучающем сайте',
        'button': 'Нажми на кнопку что бы получить новости',
        'news': news,
    }
    return render(request, 'news/news_home.html', data)

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_views.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-update.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == "POST":
        article_form = ArticlesForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('news_home')
        else:
            error = "Error"

    article_form = ArticlesForm()
    data = {
        'title': 'Форма по добавлению статьи',
        'article_form': article_form,
        'error': error,
        'article': 'Добавить статью',
    }
    return render(request, "news/create.html", data)
