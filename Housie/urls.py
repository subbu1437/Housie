from django.urls import path,include
urlpatterns=[
        path('chat/',include('wsfirstapp.urls')),
]