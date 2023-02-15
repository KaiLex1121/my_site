from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def show_mainpage(request):
    response = render_to_string('blog_app/index.html')
    return HttpResponse(response)


def show_blogpage(request):
    return render(request, 'blog_app/posts.html')


def show_post_by_name(request, post_name):
    return HttpResponse(f'Информация о посте {post_name}')


def show_post_by_number(request, post_number):
    return HttpResponse(f'Информация о посте под номером {post_number}')
