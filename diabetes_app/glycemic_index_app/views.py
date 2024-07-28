from django.http import HttpResponse
from django.shortcuts import render

from .models import CustomUser, Note, Statistics

def index(request):
    notes = Note.objects.all()
    context = {'notes': notes, 'title': 'Список записей'}
    return render(request, 'glycemic_index_app/main.html', context=context)