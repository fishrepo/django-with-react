from django.contrib import admin
from .models import Post

# admin.site.register(Post)


# class PostAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Post, PostAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'is_public',
                    'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    search_fields = ['message']
    list_filter = ['created_at', 'is_public']

    def message_length(self, post):
        return f"{len(post.message)} 글자"
