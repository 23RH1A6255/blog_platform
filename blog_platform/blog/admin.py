from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'