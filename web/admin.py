# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import csv
from django.http import HttpResponse
from django.contrib import admin
from web.models import Todo
from web.data_handler import DataManager


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'status', 'created_date', 'modified_date', 'is_active')
    list_filter = ('status', 'date', 'time')
    search_fields = ('title',)
    actions = ['get_entries']

    def get_entries(self, request, queryset):
        self.message_user(request, 'Data collected successfully')
        report = HttpResponse(content_type='text/csv')
        report['Content-Disposition'] = 'attachment; filename=todo-list-%s.csv' % (
                                                    datetime.date.today()
                                                )
        data = DataManager(queryset).get_data()
        writer = csv.writer(report)
        for entry in data:
            writer.writerow(entry)
        return report

    get_entries.short_description = 'Generate reports'

# Register your models here.
admin.site.register(Todo, TodoAdmin)
