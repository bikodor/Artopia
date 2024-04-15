from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.urls import resolve
from .models import File
# Create your views here.

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Боты', 'url_name': 'bots'},
    {'title': 'Автотесты', 'url_name': 'autotests'},
    {'title': 'Картины', 'url_name': 'pictures'},
    # {'title': 'Игры', 'url_name': 'games'},
    {'title': 'Сайты', 'url_name': 'sites'},
    {'title': 'QA Сертификаты', 'url_name': 'QA'},
    {'title': 'Leetcode', 'url_name': 'leetcode'},
]

class WomenHome(TemplateView):

    template_name = 'art/main.html'
    extra_context = {'menu': menu}




def page_not_found(request, exception=None):
    return render(request, 'art/page_not_found.html', {}, status=404)


class Pictures(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='picture')
    extra_context = {'menu': menu, 'title': 'Картины', 'posts': posts}

class Games(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='game')
    extra_context = {'menu': menu, 'title': 'Игры', 'posts': posts}

class Bots(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='bot')
    extra_context = {'menu': menu, 'title': 'Боты', 'posts': posts}

class AutoTests(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='autotest')

    extra_context = {'menu': menu, 'title': 'Автотесты', 'posts': posts}

class Sites(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='site')

    extra_context = {'menu': menu, 'title': 'Сайты', 'posts': posts}

class LeetCode(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='leetcode')
    extra_context = {'menu': menu, 'title': 'Leetcode', 'posts': posts}

class SertificatesQA(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='certificate')
    extra_context = {'menu': menu, 'title': 'QA Сертификаты', 'posts': posts}

class DataScience(TemplateView):
    template_name = 'art/languages.html'
    posts = File.objects.filter(type='data_science')
    extra_context = {'menu': menu, 'title': 'Data Science', 'posts': posts}



# class Books(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='book')
#
#     extra_context = {'menu': menu, 'title': 'Книги', 'posts': posts}
#
# class Music(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='music')
#
#     extra_context = {'menu': menu, 'title': 'Музыка', 'posts': posts}
#
# class Videos(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='video')
#     extra_context = {'menu': menu, 'title': 'Видео', 'posts': posts}