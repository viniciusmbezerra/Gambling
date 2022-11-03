from django.urls import path

from MegaSena import views
from MegaSena.views.home_view import bet, my_bets

app_name = "MegaSena"

urlpatterns = [
    path('', views.home, name='home'),
    path('bet/<int:id>/', views.bet,name='bet'),
    path('my_bets/', views.my_bets,name='my_bets'),
]
