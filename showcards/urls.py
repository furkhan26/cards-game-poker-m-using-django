from django.urls import path
from .views import *

urlpatterns = [
    path('',ShowCards, name='show_cards'),
     path('register/',registerPage,name="register"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutUser,name="logout"),
]
