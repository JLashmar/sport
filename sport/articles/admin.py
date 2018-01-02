from django.contrib import admin
from .models import Post, VideoNews


@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'post_category', 'headline_image', 'post_image', 'posted','team_a','team_b')
    prepopulated_fields = {'post_slug': ('title',)}

admin.site.register(VideoNews)
