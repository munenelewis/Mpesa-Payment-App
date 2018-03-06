from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from .views import authenticate

urlpatterns = [
    url(r'^get_token/$',
        view=authenticate,
        name="get-mpesa-token-request",),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])

"""    url(r'^request/delete/(?P<permission_pk>\d+)/$',
        view=delete_permission,
        name="authority-delete-permission-request",
        kwargs={'approved': False}),"""
