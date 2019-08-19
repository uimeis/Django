"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from book.views import book, book_detail, author


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('首页')
    else:
        book_index = reverse('作者')
        return redirect(book_index)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book/', include('book.urls')),
    path('movie/', include('movie.urls'))
]
