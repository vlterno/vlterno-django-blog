# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post # наша модель из blog/models.py

# Register your models here.
admin.site.register(Post)