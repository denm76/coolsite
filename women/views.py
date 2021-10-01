from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women, Category

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


# Create your views here.
def home(request):
    return HttpResponse('Главная страница')


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cats': cats,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponseNotFound(f"Отображение статьи с id = {post_id}")


def show_category(request, category_id):
    posts = Women.objects.filter(category_id=category_id)
    if len(posts) == 0:
        raise Http404()

    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cats': cats,
        'cat_selected': category_id
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
