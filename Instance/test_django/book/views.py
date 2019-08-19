from django.http import HttpResponse


def book(request):
    return HttpResponse('书籍')

def book_detail(request, book_id):
    a = book_id
    return HttpResponse(a)

def author(request):
    a = request.GET.get('name')
    return HttpResponse(a)