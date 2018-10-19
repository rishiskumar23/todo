from django.conf.urls import url
from api.views import TodoListView, TodoDetailView

urlpatterns = [
    url(r'^todo-list/$', TodoListView.as_view(), name="todo_list_api"),
    url(r'^todo-list/(?P<todo_id>\d+)/$', TodoDetailView.as_view(), name='todo_detail_api'),
]
