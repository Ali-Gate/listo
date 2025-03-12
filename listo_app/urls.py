from django.urls import path
from .views import home, user_login, user_logout, todo_list, todo_create, todo_update, todo_delete, sign_up
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('list/', todo_list, name='todo_list'),  # Changed from 'todo/' to 'list/'
    path('create/', todo_create, name='todo_create'),
    path('update/<int:pk>/', todo_update, name='todo_update'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('sign_up/', sign_up, name='sign_up'), 
]