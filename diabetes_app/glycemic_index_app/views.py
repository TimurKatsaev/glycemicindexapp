from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import CustomUser, Note, Statistics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer

class NoteModelListView(APIView):
    def get(self, request, pk):
        try:
            item = Note.objects.get(pk=pk)
            serializer = NoteSerializer(item)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

def index(request):
    notes = Note.objects.all()
    context = {'notes': notes, 'title': 'Список записей', 'name': 'main'}
    return render(request, 'glycemic_index_app/components/main.html', context=context)

def detail(request, pk):
    notes = get_object_or_404(Note, pk=pk)
    context = {'notes': notes, 'list': notes.glycemic_index.split(","), 'title': 'Запись', 'name': 'detail'}
    return render(request, 'glycemic_index_app/components/detail.html', context=context)

def add(request):
    context = {'title': 'Добавить запись', 'name': 'add'}
    return render(request, 'glycemic_index_app/components/add.html', context=context)

def stat(request):
    context = {'title': 'Статистика', 'name': 'stat'}
    return render(request, 'glycemic_index_app/components/stat.html', context=context)

def login(request):
    context = {'title': 'Вход', 'name': 'login'}
    return render(request, 'glycemic_index_app/components/login.html', context=context)

def personal_data(request):
    context = {'title': 'Личные данные', 'name': 'personal_data'}
    return render(request, 'glycemic_index_app/components/personal_data.html', context=context)

def setts(request):
    context = {'title': 'Настройки', 'name': 'settings'}
    return render(request, 'glycemic_index_app/components/settings.html', context=context)

def signup(request):
    context = {'title': 'Регистрация', 'name': 'signup'}
    return render(request, 'glycemic_index_app/components/signup.html', context=context)