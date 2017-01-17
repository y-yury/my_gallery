from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'
    queryset = Photo.objects.all()
    template_name = 'gallery/base.html'