from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'caption', 'created_at']
    list_filter = ['created_at']
    search_fields = ['caption', 'author__username']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'author__username']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user']
    search_fields = ['user__username', 'post__id']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
