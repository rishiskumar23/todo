from rest_framework import serializers
from web.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'date', 'time', 'todo_status', 'created_date', 'modified_date', 'url')