from django.urls import path
from . import views


urlpatterns = [
    path('beautiful_table', views.show_beautiful_table, name='beautiful_table'),
    path('kianu_rivz/', views.show_kianu_rivz_post, name='kianu'),
    path('guinnes_records/', views.show_guinness_world_records, name='guinnes_records'),
    path('<int:post_number>/', views.show_post_by_number),
    path('<str:post_name>/', views.show_post_by_name),
    path('', views.show_blogpage),
]
