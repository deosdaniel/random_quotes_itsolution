from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes_list, name='quotes_list'),
    path('random_quote/', views.random_quote, name='random_quote'),
    path('add/', views.add_quote, name='add_quote' ),
]
