from . import views
from django.urls import path,include
urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]