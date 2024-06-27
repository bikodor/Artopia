from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.urls import resolve
from .models import File
# Create your views here.

menu = [
    {'title': 'Bots', 'url_name': 'bots'},
    {'title': 'Autotests', 'url_name': 'autotests'},
    {'title': 'Pictures', 'url_name': 'pictures'},
    # {'title': 'Games', 'url_name': 'games'},
    # {'title': 'Sites', 'url_name': 'sites'},
    {'title': 'QA Certificates', 'url_name': 'QA'},
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
    extra_context = {'menu': menu, 'title': 'Pictures', 'posts': posts}

# class Games(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='game')
#     extra_context = {'menu': menu, 'title': 'Games', 'posts': posts}

class Bots(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='bot')
    extra_context = {'menu': menu, 'title': 'Bots', 'posts': posts}

class AutoTests(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='autotest')

    extra_context = {'menu': menu, 'title': 'Autotests', 'posts': posts}

# class Sites(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='site')
#
#     extra_context = {'menu': menu, 'title': 'Sites', 'posts': posts}

class LeetCode(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='leetcode')
    extra_context = {'menu': menu, 'title': 'Leetcode', 'posts': posts}

class SertificatesQA(TemplateView):
    template_name = 'art/index.html'
    posts = File.objects.filter(type='certificate')
    extra_context = {'menu': menu, 'title': 'QA Certificates', 'posts': posts}





# class Books(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='book')
#
#     extra_context = {'menu': menu, 'title': 'Books', 'posts': posts}
#
# class Music(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='music')
#
#     extra_context = {'menu': menu, 'title': 'Music', 'posts': posts}
#
# class Videos(TemplateView):
#     template_name = 'art/index.html'
#     posts = File.objects.filter(type='video')
#     extra_context = {'menu': menu, 'title': 'Videos', 'posts': posts}