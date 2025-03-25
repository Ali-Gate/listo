from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,
                               'You have been successfully logged in.')
                return redirect('todo_list')
            else:
                messages.error(request,
                               'Invalid username or password.')
        else:
            messages.error(request,
                           ('Invalid form submission. '
                            'Please check your credentials.'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(owner=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('home')
    return render(request, 'logout_confirm.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                         'Account created successfully! Please login.')
            return redirect('login')
        else:
            messages.error(request,
                           ('Invalid form submission. '
                            'Please check the errors below.'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def todo_create_or_update(request, pk=None):
    if pk:
        # Ensure the task belongs to the logged-in user
        todo = get_object_or_404(
            TodoItem, pk=pk, owner=request.user)
    else:
        todo = None

    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user  # Set the owner to the logged-in user
            todo.save()
            if pk:
                messages.success(request, 'Task updated successfully!')
            else:
                messages.success(request, 'Task created successfully!')
            return redirect('todo_list')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})


def todo_delete(request, pk):
    # Ensure the task belongs to the logged-in user
    todo = get_object_or_404(TodoItem, pk=pk, owner=request.user)
    if request.method == 'POST':
        try:
            todo.delete()
            messages.success(request, 'Task deleted successfully!')
            return redirect('todo_list')
        except Exception as e:
            messages.error(request, f'Error deleting task: {str(e)}')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
