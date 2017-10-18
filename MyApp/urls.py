from django.conf.urls import url
from .views import (hacker, hell, check_filter_tag, test_cycle, regrp)

urlpatterns = [
    url(r'^all$', hacker, name='hacker'),
    url(r'^list_all$', hell, name='hell'),
    url(r'^filt$', check_filter_tag, name='filter_check'),
    url(r'^cycl$', test_cycle, name='test_cycle'),
    url(r'regrp$', regrp, name='regrp'),
]
