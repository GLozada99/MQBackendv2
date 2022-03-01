from django.urls import path

from apps.products.views import ProductViewSet

products_urls = [
     path('products',
          ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
     path('products/<int:pk>',
          ProductViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                  'put': 'update',
                                  'patch': 'partial_update'})),
]
