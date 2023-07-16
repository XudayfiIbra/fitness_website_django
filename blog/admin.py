from django.contrib import admin
from .models import Category


#Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'created_by')


admin.site.register(Category)

