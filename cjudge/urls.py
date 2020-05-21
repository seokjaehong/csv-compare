from django.conf.urls import url

from cjudge.views import submission_list

urlpatterns = [
    url(r'^list/$', submission_list, name='submission_list'),
]
