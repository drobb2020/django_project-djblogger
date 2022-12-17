from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at')
    search_fields = ['title', 'status',]
    prepopulated_fields = {
        'slug': ('title', )
    }
    list_filter = ('author', 'status', 'created_at')

# admin.site.register(Post)
