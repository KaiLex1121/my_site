from django.shortcuts import render
from django.http import HttpResponse


def show_mainpage(request):
    return HttpResponse('Главная страница')


def show_blogpage(request):
    return HttpResponse('Все посты блога')

def show_posts(request, post_name=None):
    return HttpResponse(f'Информация о посте {post_name}')
