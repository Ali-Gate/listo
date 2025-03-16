from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import TodoItem
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'owner')
    search_fields = ('title', 'owner__username')
    list_filter = ('completed', 'due_date', 'owner')

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 1

class CustomUserAdmin(BaseUserAdmin):
    inlines = [TodoItemInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'view_tasks_link')

    def view_tasks_link(self, obj):
        url = reverse('admin:listo_app_todoitem_changelist') + f'?owner__id__exact={obj.id}'
        return format_html('<a href="{}">View Tasks</a>', url)
    view_tasks_link.short_description = 'Tasks'

# Register your models here.
admin.site.register(TodoItem, TodoItemAdmin)  # Register TodoItem with TodoItemAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin) # Added this line, Register User with CustomUserAdmin