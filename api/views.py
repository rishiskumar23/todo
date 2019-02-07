# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from django.views.generic import View
from django.http import JsonResponse
from web.models import Todo
from api.serializers import TodoSerializer


# class TodoListView(View):
#     http_method_names = ['get', 'options']

#     def get(self, request, *args, **kwargs):
#         todo_list = Todo.objects.filter(is_active=True).order_by('date', 'time')
#         data = [{
#             'id': todo.id,
#             'title': todo.title,
#             'description': todo.description,
#             'date': todo.date,
#             'time': todo.time,
#             'status': todo.get_status(),
#             'created_date': todo.created_date,
#             'modified_date': todo.modified_date,
#             'url': todo.get_api_url()
#         } for todo in todo_list]
#         return JsonResponse({
#                 'message': 'success',
#                 'data': data
#             }, status=200)


# class TodoDetailView(View):
#     http_method_names = ['get', 'options']

#     def get(self, request, *args, **kwargs):
#         todo_id = kwargs.get('todo_id')
#         try:
#             todo_item = Todo.objects.get(id=todo_id)
#         except Todo.DoesNotExist:
#             return JsonResponse({
#                     'error': {
#                         'message': 'Todo item doesnot exits'
#                     }
#                 }, status=400)
#         item_data = {
#             'id': todo_item.id,
#             'title': todo_item.title,
#             'description': todo_item.description,
#             'date': todo_item.date,
#             'time': todo_item.time,
#             'status': todo_item.get_status(),
#             'created_date': todo_item.created_date,
#             'modified_date': todo_item.modified_date,
#         }
#         return JsonResponse({
#                 'message': 'success',
#                 'data': item_data
#             }, status=200)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(is_active=True).order_by('date', 'time')
    serializer_class = TodoSerializer