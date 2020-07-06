from django.contrib import admin
from website.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'full_name']
    search_fields = ['title', 'subtitle']
    fields = ('title', 'subtitle')


admin.site.register(Post, PostAdmin)
