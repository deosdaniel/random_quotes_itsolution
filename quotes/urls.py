from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='quotes_list'),
    path('add/', views.add_quote, name='add_quote'),
    path('quote/<int:pk>', views.quote_detail, name='quote_detail'),
    path('random_quote/', views.random_quote, name='random_quote'),
    path('like/<int:pk>', views.like_quote, name='like_quote'),
    path('dislike/<int:pk>', views.dislike_quote, name='dislike_quote'),
]
