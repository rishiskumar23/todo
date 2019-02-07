# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from web.utilts import get_site_url_without_scheme

try:
    domain = get_site_url_without_scheme()
except:
    domain = ""


class Todo(models.Model):

    INPROGRESS = 'I'
    COMPLETED = 'C'
    PENDING = 'P'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (INPROGRESS, 'In-progress'),
        (COMPLETED, 'Completed'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='P')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "To-do item"
        verbose_name_plural = "To-do items"

    def __str__(self):
        return self.title

    def todo_status(self):
        if self.status == self.INPROGRESS:
            return 'In-progress'
        elif self.status == self.COMPLETED:
            return 'Completed'
        elif self.status == self.PENDING:
            return 'Pending'
        else:
            return None

    def get_slug(self):
        slug = slugify(self.title)
        return slug

    # def get_api_url(self):
    #     return (domain + reverse('todo_detail_api', args=(self.id,)))
