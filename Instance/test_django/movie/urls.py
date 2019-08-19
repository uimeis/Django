from django.urls import path
from .views import index, detail, add_movie, dele_movie

urlpatterns = [
    path('', index, name='电影首页'),
    path('add_movie/', add_movie, name='发布电影'),
    path('detail/<int:movie_id>/', detail, name='电影详情'),
    path('del_movie/', dele_movie, name='删除电影')
]