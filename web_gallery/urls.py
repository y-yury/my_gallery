from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from gallery.views import PhotoListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PhotoListView.as_view(), name='photo_list'),
    url(r'^accounts/login/$', views.login, name="login"),
    url(r'^accounts/logout$', views.logout, name="logout", kwargs={'next_page': '/'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
