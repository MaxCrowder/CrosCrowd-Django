from django.urls import path
from . import views


urlpatterns = [
    path('', views.advertising)
    # path('project1/', views.project1)
]