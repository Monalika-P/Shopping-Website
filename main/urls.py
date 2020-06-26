
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('collection', views.collection, name = 'collection'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),

]
