from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from api.views.base import BaseViewSet
from apps.products.models import Product
from apps.products.serializers import BasicProductSerializer


class ProductViewSet(BaseViewSet):
    model = Product
    serializer = BasicProductSerializer

    @swagger_auto_schema(
        operation_description='Lists Products',
        responses={status.HTTP_200_OK: BasicProductSerializer(many=True)})
    def list(self, request):
        return super().list(request)

    @swagger_auto_schema(
        operation_description='Get details of a Product object',
        responses={status.HTTP_200_OK: BasicProductSerializer})
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(
        operation_description='Creates Product',
        request_body=BasicProductSerializer,
        responses={status.HTTP_200_OK: BasicProductSerializer})
    def create(self, request):
        return super().create(request)

    @swagger_auto_schema(
        operation_description='Updates Product',
        request_body=BasicProductSerializer,
        responses={status.HTTP_200_OK: BasicProductSerializer})
    def update(self, request):
        return super().update(request)

    @swagger_auto_schema(
        operation_description='Partially Updates Product',
        request_body=BasicProductSerializer,
        responses={status.HTTP_200_OK: BasicProductSerializer})
    def partial_update(self, request):
        return super().partial_update(request)

    @swagger_auto_schema(
        operation_description='Deletes a Product object',
        responses={status.HTTP_200_OK: BasicProductSerializer})
    def destroy(self, request, pk=None):
        return super().destroy(request, pk)
