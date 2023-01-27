from django.shortcuts import render
from django.http import HttpResponse


def show_mainpage(request):
    return HttpResponse('Главная страница')

def show_blogpage(request):
    return HttpResponse('Список постов блога')