from django.urls import path

from todo_app import views
from todo_app.views import index

urlpatterns = [
    path('home/', index),
    path('', views.home, name='home'),
]