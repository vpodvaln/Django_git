from django.conf.urls import url, include
from django.contrib import admin
from pre_order import views

urlpatterns = [
    url(r'^pre_order/', views.pre_order, name='pre_order'),
]