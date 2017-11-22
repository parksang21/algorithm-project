from django.conf.urls import url
from .views import attendance_check



urlpatterns = [
    url(r'^$', attendance_check, name='main'),
]