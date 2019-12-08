from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.show_map),
    path('add/', views.add_squirrel),
    path('<int:Unique_Squirrel_ID>/', views.edit_squirrel),
    path('', views.all_squirrel),
]