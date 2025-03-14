from django.urls import path
from .views import home, user_login, user_logout, todo_list, todo_create, todo_update, todo_delete, signup
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('list/', todo_list, name='todo_list'),  # Changed from 'todo/' to 'list/'
    path('create/', todo_create, name='todo_create'),
    path('update/<int:pk>/', todo_update, name='todo_update'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('signup/', signup, name='signup'), 
]