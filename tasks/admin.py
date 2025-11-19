from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'priority', 'is_completed')
    search_fields = ('title',)


admin.site.register(models.Task, TaskAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


admin.site.register(models.Category, CategoryAdmin)
