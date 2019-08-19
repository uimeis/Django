from django.urls import path
from .views import book, book_detail, author

urlpatterns = [
    path('', book, name='book'),
    path('detail/<book_id>', book_detail, name='图书详情'),
    path('author/', author, name='作者')
]