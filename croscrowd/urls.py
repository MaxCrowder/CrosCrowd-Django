from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('webdevelopment/', include('webdev.urls')),
    path('advertising/', include('advertising.urls')),
    path('consulting/', include('consulting.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]

urlpatterns += staticfiles_urlpatterns()
