from django.urls import path
from .views import ThreadList, ThreadDetail

messenger_paterns = ([
                         path('', ThreadList.as_view(), name='list'),
                         path('thread/<int:pk>/', ThreadDetail.as_view(), name='detail'),
                     ], "messenger")
