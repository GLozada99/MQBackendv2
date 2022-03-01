from django.urls import path

from apps.quotes.views import QuoteViewSet, InvoiceViewSet

people_urls = [
     path('products',
          QuoteViewSet.as_view({'get': 'list', 'post': 'create'})),
     path('products/<int:pk>',
          QuoteViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
     path('products/<int:pk>/client',
          QuoteViewSet.as_view({'get': 'retrieve_client'})),
     path('products/<int:pk>/products',
          QuoteViewSet.as_view({'get': 'list_products'})),
     path('invoice',
          InvoiceViewSet.as_view({'get': 'list', 'post': 'create'})),
     path('invoice/<int:pk>',
          InvoiceViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
     path('invoice/<int:pk>/quote',
          InvoiceViewSet.as_view({'get': 'retrieve_client'})),

]
