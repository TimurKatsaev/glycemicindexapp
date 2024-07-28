from django.contrib import admin
from .models import CustomUser, Note, Statistics

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'general_gi', 'general_rcg')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(CustomUser)
admin.site.register(Note, NoteAdmin)
admin.site.register(Statistics)