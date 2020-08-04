from django.urls import re_path

from wsfirstapp import consumer

websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<person_name>\w+)/$',consumer.Consumer)
]