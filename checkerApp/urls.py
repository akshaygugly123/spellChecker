from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('populate/', views.populateDB, name='populate'),
    path('delete_every_word/', views.delete_every_word, name='delete_every_word'),
    path('search_result/', views.search_result, name='search_result'),
]
