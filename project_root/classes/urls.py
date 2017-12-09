from django.conf.urls import url
from django.shortcuts import redirect

from .views import today_class, class_detail

urlpatterns = [
    url(r'^(?P<id>\d+)/$', today_class, name="class_list"),
    url(r'^detail/(?P<id>\d+)/$', class_detail, name="class_detail"),
]