from django.urls import path,include
from Housie.views import Index
urlpatterns=[

        path('',Index.as_view()),
        path('chat/',include('wsfirstapp.urls')),
        path('user/',include('usermanagement.urls'))
]