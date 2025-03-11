from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete
from . import views


urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('update/<int:pk>/', todo_update, name='todo_update'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
]