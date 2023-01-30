from django.urls import path
from . import views


urlpatterns = [
    path('<int:post_number>/', views.show_post_by_number),
    path('<str:post_name>/', views.show_post_by_name),
    path('', views.show_blogpage)
]
