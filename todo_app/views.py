from http.client import HTTPResponse

from asgiref.typing import HTTPRequestEvent
from django.http import HttpResponse

from django.shortcuts import render
from todo_app.models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def home(request):
    return HttpResponse("Hello, world! This is the home page.")