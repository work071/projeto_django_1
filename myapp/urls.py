from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpRequest
from myapp.views import HOME

urlpatterns = [
    path('', HOME),

]
