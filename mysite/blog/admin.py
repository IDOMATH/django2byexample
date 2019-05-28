from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #Fields to display in admin site under the Post
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    #Fields to filter by on admin site
    list_filter = ('status', 'created', 'publish', 'author')
    #Which fields the search looks through
    search_fields = ('title', 'body')
    #Automatically fills in slug field based on title
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author',)
    #Navigation links that appear under the search bar
    date_hierarchy = 'publish'
    #Specifying the default attributes to order by
    ordering = ('status', 'publish')