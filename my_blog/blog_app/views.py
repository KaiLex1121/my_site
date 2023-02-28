from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from random import sample


def get_posts():

    posts = [
        {
            'title': 'Рыбалка',
            'description': 'Хорошо посидели',
            'date': '21 авг 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
        },
        {
            'title': 'Париж',
            'description': 'Незабываемое путешествие',
            'date': '5 сент 2020',
            'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
        },
        {
            'title': 'Финал лиги чемпионов',
            'description': 'Реал опять выиграл ЛЧ',
            'date': '28 мая 2022',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
        },
        {
            'title': 'Охота на уток',
            'description': 'Ни одна утка не пострадала',
            'date': '7 дек 2019',
            'content': 'Lorem ipsum dolor sit amet.'
        },
        {
            'title': 'Фестиваль огурца',
            'description': 'Суздаль ждет тебя',
            'date': '12 июль 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
        },
        {
            'title': 'Нашествие',
            'description': 'Даешь рок, но в следующем году',
            'date': '29 июль 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
        },
        {
            'title': 'Новый год',
            'description': 'Эх, еще один год пролетел',
            'date': '31 дек 2022',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
        },
    ]

    return posts


def show_mainpage(request):

    chosen_posts = sample(get_posts(), 3)

    context_data = {
        'posts': chosen_posts
    }

    return render(request, 'blog_app/index.html', context=context_data)


def show_blogpage(request):

    context_data = {
        'posts': get_posts()
    }

    return render(request, 'blog_app/posts.html', context=context_data)


def show_post_by_name(request, post_name):

    post_name = post_name.lower()

    response = None

    if post_name == 'киану_ривз':
        response = reverse('kianu')

    elif post_name == 'рекорды_гиннеса':
        response = reverse('guinnes_records')

    elif post_name == 'красивая_табличка':
        response = reverse('beautiful_table')

    if response is not None:
        return HttpResponseRedirect(response)

    return HttpResponse(f'Поста {post_name} пока не существует')


def show_post_by_number(request, post_number):

    return render(request, 'blog_app/post_by_number.html', context={'post_number': post_number})


def show_guinness_world_records(request):

    context_data = {
        'power_man': 'Narve Laeret',
        'bar_name': "Bob’s BBQ & Grill",
        'count_needle': 1790,
    }

    return render(request, 'blog_app/guinnes_records.html', context=context_data)


def show_kianu_rivz_post(request):

    context_data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Матрица'
    }

    return render(request, 'blog_app/kianu_rivz_post.html', context=context_data)


def show_beautiful_table(request):

    return render(request, 'blog_app/beautiful_table.html')
