from django.shortcuts import render
from todos.models import Todo
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from todos.pagination import CustomPageNumberPagination

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete']
    search_fields = ['id', 'title', 'is_complete']
    oredering_fields = ['id', 'title', 'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user,)


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class ListTodoAPIView(ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user,)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user,)