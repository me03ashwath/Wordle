from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('play/', views.playGame, name='playgame'),
    path('logout/', views.logoutUser, name='logout'),
    path('add-words/', views.addWords),
]