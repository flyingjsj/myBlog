from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', about),
    path('gbook/', gbook),
    path('index/', index),
    path('info/', info),
    path('list/', list),
]
