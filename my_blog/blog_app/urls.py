from django.urls import path
from . import views


urlpatterns = [
    path('<post_name>/', views.show_posts),
    path('', views.show_blogpage)
]
