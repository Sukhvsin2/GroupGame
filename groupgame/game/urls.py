from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('game/<u_name>/<game_id>/', GameView.as_view(), name='GameView'),
]
