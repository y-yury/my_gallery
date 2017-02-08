from django.contrib import admin
from .models import Photo, Profile, Email


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'timestamp',)
    list_display_links = ('title',)
    search_fields = ('author','title',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'city', 'country',)
    list_display_links = ('user',)
    search_fields = ('user','name',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'e_mail', 'message',)
    list_display_links = ('name',)
    search_fields = ('name', 'e_mail',)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Email, EmailAdmin)