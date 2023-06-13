from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('upload/',views.upload_file, name='upload_file'),
    path('views/', views.view_files, name='view_files'),
]

