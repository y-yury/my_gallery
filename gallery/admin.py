from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(Photo, PhotoAdmin)