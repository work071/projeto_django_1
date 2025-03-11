from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, HttpRequest
from myapp.views import HOME

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls")),

]
