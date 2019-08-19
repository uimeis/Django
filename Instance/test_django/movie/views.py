from django.shortcuts import render, redirect, reverse
from django.db import connection

# Create your views here.
def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    # cursor.execute("insert into movie(id,name,author) values(2,'哪吒','童夏')")
    cursor.execute("select id,name,author from movie")
    movies = cursor.fetchall()
    context = {'movies': movies}
    return render(request, 'index.html', context=context)

def add_movie(request):
    if request.method == 'GET':
        return render(request, 'add_movie.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into movie(id,name,author) values(null,'{}','{}')".format(name, author))
        return redirect(reverse('电影首页'))

def detail(request, movie_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author from movie where id='{}'".format(movie_id))
    movie = cursor.fetchone()
    context = {'movie':movie}
    return render(request, 'detail.html', context=context)

def dele_movie(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        cursor = get_cursor()
        cursor.execute("delete from movie where id='{}'".format(movie_id))
        return redirect(reverse('电影首页'))
    else:
        raise RuntimeError('错误')
