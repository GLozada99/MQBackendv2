from django.urls import path

from apps.people.views import ClientViewSet

people_urls = [
     path('client',
          ClientViewSet.as_view({'get': 'list', 'post': 'create'})),
     path('client/<int:pk>',
          ClientViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                 'put': 'update',
                                 'patch': 'partial_update'})),
]
