from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display: tuple = ('title', 'owner', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display: tuple = ('body', 'owner', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
