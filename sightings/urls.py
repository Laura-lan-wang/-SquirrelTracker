from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.show_map),
    path('add/', views.add_squirrel),
    path('stats/', views.show_stats),
    path('<str:sq_ID>/', views.edit_squirrel),
    path('', views.all_squirrel),
]