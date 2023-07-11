from models import TableTodo
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableTodo
        fields = ['task_name', 'task_status', 'task_description']