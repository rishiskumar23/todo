# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (DetailView, CreateView, ListView,
                                  DeleteView, UpdateView)
from web.models import Todo
from web.forms import TodoForm


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    ordering = ['date', 'time']

    def get_queryset(self):
        ordering = self.get_ordering()
        return self.model.objects.filter(is_active=True).order_by(*ordering)


class TodoDetailView(DetailView):
    model = Todo
    slug_url_kwarg = None
    pk_url_kwarg = 'todo_id'


class TodoDeleteView(DeleteView):
    model = Todo
    slug_url_kwarg = None
    pk_url_kwarg = 'todo_id'
    success_url = reverse_lazy('todo_list')

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        item.is_active = False
        item.save()
        return HttpResponseRedirect(self.success_url)


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

    def get_context_data(self, **kwargs):
        context = super(TodoCreateView, self).get_context_data(**kwargs)
        context.update({
                'form_title': "Add To-do item"
            })
        return context


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    slug_url_kwarg = None
    pk_url_kwarg = 'todo_id'
    success_url = reverse_lazy('todo_list')

    def get_context_data(self, **kwargs):
        context = super(TodoUpdateView, self).get_context_data(**kwargs)
        context.update({
                'form_title': "Edit To-do item"
            })
        return context
