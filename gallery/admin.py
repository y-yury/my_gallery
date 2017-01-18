from django.contrib import admin
from .models import Photo, Profile


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'timestamp',)
    list_display_links = ('title',)
    search_fields = ('author','title',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'city', 'country',)
    list_display_links = ('user',)
    search_fields = ('user','name',)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Profile, ProfileAdmin)