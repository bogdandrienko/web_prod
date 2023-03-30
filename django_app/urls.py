from django.contrib import admin
from django.urls import path, include, re_path
from django_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name=""),
    re_path(r"users/(?P<pk>\d+)/$", views.users_f),
]
