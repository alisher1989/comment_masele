from django.contrib import admin

from webapp.models import Post, Comment, PostsComments


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at', 'author']
    list_filter = ['title']
    search_fields = ['title', 'text']
    fields = ['title', 'text', 'created_at', 'author']
    readonly_fields = ['created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostsComments)