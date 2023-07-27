from django.contrib import admin
from .models import Category, Post


#Category
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'created_by', 'created_date')


admin.site.register(Category, CategoryAdmin)


#Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'content', 'published', 'tags', 'created_by')
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Post,PostAdmin)



