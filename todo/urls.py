"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import api.urls
from django.conf.urls import url, include
from django.contrib import admin
from web.views import (TodoListView, TodoDetailView, TodoDeleteView, TodoCreateView,
                       TodoUpdateView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(api.urls)),
    url(r'^$', TodoListView.as_view(), name="todo_list"),
    url(r'^add/$', TodoCreateView.as_view(), name="todo_create"),
    url(r'^(?P<todo_slug>[-\w]*)/(?P<todo_id>\d+)/$', TodoDetailView.as_view(), name="todo_detail"),
    url(r'^(?P<todo_slug>[-\w]*)/(?P<todo_id>\d+)/delete/$', TodoDeleteView.as_view(), name="todo_delete"),
    url(r'^(?P<todo_slug>[-\w]*)/(?P<todo_id>\d+)/edit/$', TodoUpdateView.as_view(), name="todo_update"),
]
