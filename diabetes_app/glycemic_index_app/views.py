from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import CustomUser, Note, Statistics
from .forms import SignUpForm, EditingForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.shortcuts import render, redirect

from .forms import NoteForm

class NoteModelListView(APIView):
    def get(self, request, pk):
        try:
            item = Note.objects.get(pk=pk)
            serializer = NoteSerializer(item)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@login_required(login_url='glycemic_index_app:login')
def index(request):
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes, 'title': 'Список записей', 'name': 'main'}
    return render(request, 'glycemic_index_app/components/main.html', context=context)

@login_required(login_url='glycemic_index_app:login')
def detail(request, pk):
    notes = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = EditingForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('glycemic_index_app:main')  # перенаправление на страницу с записью после сохранения
    else:
        form = EditingForm(instance=notes)
    context = {'notes': notes, 'list': notes.glycemic_index.split(","), 'title': 'Запись', 'name': 'detail', 'form': form}
    return render(request, 'glycemic_index_app/components/detail.html', context=context)

@login_required(login_url='glycemic_index_app:login')
def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Сначала не сохраняем в базу данных
            note.user = request.user  # Назначаем текущего пользователя
            note.save()  # Сохраняем объект в базу данных
            return redirect('glycemic_index_app:main')  # замените на ваш путь
    else:
        form = NoteForm()
    context = {'title': 'Добавить запись', 'name': 'add', 'form': form}
    return render(request, 'glycemic_index_app/components/add.html', context=context)

@login_required(login_url='glycemic_index_app:login')
def stat(request):
    context = {'title': 'Статистика', 'name': 'stat'}
    return render(request, 'glycemic_index_app/components/stat.html', context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
            if user is not None:
                login(request, user)
                return redirect('glycemic_index_app:main')
    else:
        form = AuthenticationForm()
    context = {'title': 'Вход', 'name': 'login', 'form': form}
    return render(request, 'glycemic_index_app/components/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('glycemic_index_app:main')

@login_required(login_url='glycemic_index_app:login')
def personal_data(request):
    context = {'title': 'Личные данные', 'name': 'personal_data'}
    return render(request, 'glycemic_index_app/components/personal_data.html', context=context)

@login_required(login_url='glycemic_index_app:login')
def setts(request):
    context = {'title': 'Настройки', 'name': 'settings'}
    return render(request, 'glycemic_index_app/components/settings.html', context=context)

def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Обновляем экземпляр пользователя с помощью данных из формы
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('glycemic_index_app:main')
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
    else:
        form = SignUpForm()
    context = {'title': 'Регистрация', 'name': 'signup', 'form': form}
    return render(request, 'glycemic_index_app/components/signup.html', context=context)