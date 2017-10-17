from django.conf.urls import url
from .views import hacker, hell

urlpatterns = [
    url(r'^all$', hacker, name='hacker'),
    url(r'^list_all$', hell, name='hell'),
]
