from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_mainpage),
    path('blog/', views.show_blogpage)
]
