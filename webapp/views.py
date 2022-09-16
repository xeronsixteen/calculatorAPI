import json

from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here

from django.views.decorators.csrf import ensure_csrf_cookie


def index_view(request):
    return render(request, 'index2.html')


def string_checker(string):
    if not string.isdigit():
        response = JsonResponse({'error': f'{string} number not integer'})
        response.status_code = 400
        return response
    else:
        return string


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def add_numbers(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': (f'{b} not integer')})
        response.status_code = 400
        return response
    c = int(a) + int(b)
    answer = {"answer": c}
    return JsonResponse(answer)


def subtract_numbers(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': (f'{b} not integer')})
        response.status_code = 400
        return response
    c = int(a) - int(b)
    answer = {"answer": c}
    return JsonResponse(answer)


def multiply_numbers(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': (f'{b} not integer')})
        response.status_code = 400
        return response
    c = int(a) * int(b)
    answer = {"answer": c}
    return JsonResponse(answer)


def divide_numbers(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if int(b) == 0:
        response = JsonResponse({'error': (' zero division error')})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': (f'{b} not integer')})
        response.status_code = 400
        return response

    c = int(a) / int(b)
    answer = {"answer": c}
    return JsonResponse(answer)
