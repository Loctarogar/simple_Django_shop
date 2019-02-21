from django.contrib import admin
from .models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author",
                    "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["status", "publish"]

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_author", "post", "active", "created", "updated")
    list_filter = ("comment_author", "active", "created", "updated")
    search_fields = ("comment_author", "body",)

admin.site.register(Comment, CommentAdmin)