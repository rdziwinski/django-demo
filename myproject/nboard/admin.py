from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'created_on', 'updated_on')
    list_filter = ('type', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Notice, NoticeAdmin)