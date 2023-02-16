from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse


def show_mainpage(request):
    response = render_to_string('blog_app/index.html')
    return HttpResponse(response)


def show_blogpage(request):
    return render(request, 'blog_app/posts.html')


def show_post_by_name(request, post_name):

    post_name = post_name.lower()

    response = None

    if post_name == 'киану_ривз':
        response = reverse('kianu')

    elif post_name == 'рекорды_гиннеса':
        response = reverse('guinnes_records')

    if response is not None:
        return HttpResponseRedirect(response)

    return HttpResponse(f'Поста {post_name} пока не существует')


def show_guinness_world_records(request):

    context = {
        'power_man': 'Narve Laeret',
        'bar_name': "Bob’s BBQ & Grill",
        'count_needle': 1790,
    }

    return render(request, 'blog_app/guinnes_records.html', context=context)


def show_kianu_rivz_post(request):

    context_data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Матрица'
    }

    return render(request, 'blog_app/kianu_rivz_post.html', context=context_data)


def show_post_by_number(request, post_number):
    return HttpResponse(f'Информация о посте под номером {post_number}')
