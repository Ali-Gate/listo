from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create_or_update, name='todo_create'),
    path('update/<int:pk>/', views.todo_create_or_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('signup/', views.signup, name='signup'),
]
