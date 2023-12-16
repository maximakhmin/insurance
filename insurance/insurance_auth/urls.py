from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login', views.login),         # permit all
    path('register', views.register),   # permit all
    # path('refresh', views.refresh),
    path('who', views.who)              # permit all
]