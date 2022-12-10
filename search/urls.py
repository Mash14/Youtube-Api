from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.search, name='search'),
    re_path('video/(?P<slug>[\w-]+)/',views.single_item, name='searched_video')
]