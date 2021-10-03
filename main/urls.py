from django.contrib import admin
from django.urls import path
from .views import HomePage, add_item

urlpatterns = [

    path('', HomePage.as_view(), name='home'),
    path('add_item/', add_item, name='add'),
]
