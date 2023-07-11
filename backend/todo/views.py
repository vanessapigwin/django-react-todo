from rest_framework import viewsets
from rest_framework import permissions
from todo.serializers import TodoSerializer
from todo.models import TableTodo


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TableTodo.objects.all()
    permission_classes = [permissions.IsAuthenticated]