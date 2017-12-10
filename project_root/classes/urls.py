from django.conf.urls import url
from django.shortcuts import redirect

from .views import today_class, class_detail, date_detail, refresh

urlpatterns = [
    url(r'^(?P<id>\d+)/$', today_class, name="class_list"),
    url(r'^detail/(?P<id>\d+)/$', class_detail, name="class_detail"),
    url(r'^detail/(?P<c_id>\d+)/(?P<id>\d+)/$', date_detail ,name="date_detail"),
    url(r'^refresh/$', refresh, name="refresh"),
]