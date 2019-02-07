# from django.conf.urls import url

from django.conf.urls import url, include
from rest_framework import routers
from api.views import TodoViewSet


router = routers.DefaultRouter()
router.register(r'todo-list', TodoViewSet)
# router.register(r'groups', GroupViewSet)


urlpatterns = [
	url(r'/', include(router.urls)),
]
# from api.views import TodoListView, TodoDetailView

# urlpatterns = [
#     url(r'^todo-list/$', TodoListView.as_view(), name="todo_list_api"),
#     url(r'^todo-list/(?P<todo_id>\d+)/$', TodoDetailView.as_view(), name='todo_detail_api'),
# ]
