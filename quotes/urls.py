from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes_list),
    path('random_quote/', views.random_quote),
]
