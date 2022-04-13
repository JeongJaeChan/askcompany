from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'create_at', 'update_at']
    list_display_links = ['message']
    list_filter = ['create_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            # mark_safe = 이미지가 안전하다는걸 알려줌
            return mark_safe(f'<img src="{post.photo.url}" style="width: 75px;" />')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass