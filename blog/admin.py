from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titles', 'slug', 'author', 'publish', 'status',)
    list_filter = ('status', 'publish', 'created', 'author')
    search_fields = ('titles', 'body',)
    prepopulated_fields = {
        'slug': ('titles',)
    }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')
    list_editable = ('status',)
    list_display_links = ('slug', 'titles',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'updated')
    list_editable = ('active',)
    list_display_links = ('name', 'post', 'body')
