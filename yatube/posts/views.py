from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница соцсети')


def group_posts(request, pk):
    return HttpResponse(f'Группа {pk}')
