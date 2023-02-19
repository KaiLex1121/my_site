from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def show_mainpage(request):
    response = render_to_string('blog_app/index.html')
    return HttpResponse(response)


def show_blogpage(request):
    return render(request, 'blog_app/posts.html')


def show_post_by_name(request, post_name):

    context_data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Матрица'
    }

    if post_name.lower() == 'киану_ривз':
        return render(request, 'blog_app/kianu_rivz_post.html', context=context_data)


def show_post_by_number(request, post_number):
    return HttpResponse(f'Информация о посте под номером {post_number}')
