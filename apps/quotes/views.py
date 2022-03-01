from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from api.views.base import BaseViewSet
from apps.quotes.models import Quote
from apps.quotes.serializers import (BasicQuoteSerializer,
                                     ClientQuoteSerializer,
                                     ProductsQuoteSerializer)


class QuoteViewSet(BaseViewSet):
    model = Quote
    serializer = BasicQuoteSerializer
    shadow_serializer = BasicQuoteSerializer
    client_serializer = ClientQuoteSerializer
    product_serializer = ProductsQuoteSerializer

    @swagger_auto_schema(operation_description='Lists Quotes',
                         responses={status.HTTP_200_OK: BasicQuoteSerializer(
                             many=True)}
                         )
    def list(self, request):
        return super().list(request)

    @swagger_auto_schema(operation_description=
                         'Get details of a Quote object',
                         responses={status.HTTP_200_OK: BasicQuoteSerializer}
                         )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(operation_description='Creates Quote',
                         request_body=BasicQuoteSerializer,
                         responses={status.HTTP_200_OK: BasicQuoteSerializer}
                         )
    def create(self, request):
        return super().create(request)

    @swagger_auto_schema(operation_description='Updates Quote',
                         request_body=BasicQuoteSerializer,
                         responses={status.HTTP_200_OK: BasicQuoteSerializer}
                         )
    def update(self, request):
        return super().update(request)

    @swagger_auto_schema(operation_description='Partially Updates Quote',
                         request_body=BasicQuoteSerializer,
                         responses={status.HTTP_200_OK: BasicQuoteSerializer}
                         )
    def partial_update(self, request):
        return super().partial_update(request)

    @swagger_auto_schema(operation_description='Deletes a Quote object',
                         responses={status.HTTP_200_OK: BasicQuoteSerializer}
                         )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk)

    @swagger_auto_schema(operation_description=
                         'Get details of the Client on Quote',
                         responses={status.HTTP_200_OK: ClientQuoteSerializer}
                         )
    def retrieve_client(self, request, pk=None):
        self.serializer = self.client_serializer
        response = super().retrieve(request, pk)
        self.serializer = self.shadow_serializer
        return response

    @swagger_auto_schema(operation_description='Lists Products in Quote',
                         responses={status.HTTP_200_OK: ProductsQuoteSerializer(
                             many=True)}
                         )
    def list_products(self, request, pk=None):
        self.serializer = self.client_serializer
        response = super().retrieve(request, pk)
        self.serializer = self.shadow_serializer
        return response


