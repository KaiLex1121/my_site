from django.shortcuts import render
from django.http import HttpResponse


def show_mainpage(request):
    return HttpResponse('Главная страница')


def show_blogpage(request):
    return HttpResponse('Все посты блога')


def show_post_by_name(request, post_name):
    return HttpResponse(f'Информация о посте {post_name}')


def show_post_by_number(request, post_number):
    return HttpResponse(f'Информация о посте под номером {post_number}')
