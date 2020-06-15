from django.urls import path
from . import views


urlpatterns = [
    path('', views.webdev)
    # path('project1', views.project1)
]