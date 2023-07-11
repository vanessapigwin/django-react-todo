from django.contrib import admin
from .models import TableTodo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'task_name', 'task_status', 'task_description']
    

admin.site.register(TableTodo, TodoAdmin)