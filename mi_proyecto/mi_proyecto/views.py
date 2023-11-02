from django.shortcuts import render

def index(request):
    return render(request, 'mi_app/index.html')
esto en urls: from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #
]
