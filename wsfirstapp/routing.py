from django.urls import re_path

from wsfirstapp import consumer

websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/(?P<person_name>\w+)/$',consumer.Consumer)
]