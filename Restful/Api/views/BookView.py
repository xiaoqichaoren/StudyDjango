from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from Api.models import Book


@csrf_exempt
def book(request, book_id):
    if request.method == 'GET':
        books = Book.objects.all()
        books_json = list(map(lambda book: book.to_dict(), books))
        data = {
            'status': 200,
            'msg': 'ok',
            'data': books_json,
        }
        return JsonResponse(data=data)

    elif request.method == 'POST':
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')
        # b_name = '西游'
        # b_price = 32
        # print(b_name, b_price)
        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()
        data = {
            'status': 201,
            'msg': 'add success',
            'data': book.to_dict(),
        }
        return JsonResponse(data=data)

    elif request.method == 'PUT':
        b_price = request.POST.get('b_price')
        # b_price = 999.99
        print(b_price)
        book = Book.objects.get(pk=book_id)
        book.b_price = b_price
        book.save()
        data = {
            'status': 201,
            'msg': 'PUT',
            'data': book.to_dict(),
        }
        return JsonResponse(data=data)

    elif request.method == 'DELETE':
        book = Book.objects.get(pk=book_id)
        book.delete()
        data = {
            'status': 204,
            'msg': 'delete',
        }
        return JsonResponse(data=data)

