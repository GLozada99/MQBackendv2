from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from api.views.base import BaseViewSet
from apps.people.models import Client
from apps.people.serializers import BasicClientSerializer


class ClientViewSet(BaseViewSet):
    model = Client
    serializer = BasicClientSerializer

    @swagger_auto_schema(
        operation_description='Lists Clients',
        responses={status.HTTP_200_OK: BasicClientSerializer(many=True)})
    def list(self, request):
        return super().list(request)

    @swagger_auto_schema(
        operation_description='Get details of a Client object',
        responses={status.HTTP_200_OK: BasicClientSerializer})
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(
        operation_description='Creates Client',
        request_body=BasicClientSerializer,
        responses={status.HTTP_200_OK: BasicClientSerializer})
    def create(self, request):
        return super().create(request)

    @swagger_auto_schema(
        operation_description='Updates Client',
        request_body=BasicClientSerializer,
        responses={status.HTTP_200_OK: BasicClientSerializer})
    def update(self, request):
        return super().update(request)

    @swagger_auto_schema(
        operation_description='Partially Updates Client',
        request_body=BasicClientSerializer,
        responses={status.HTTP_200_OK: BasicClientSerializer})
    def partial_update(self, request):
        return super().partial_update(request)

    @swagger_auto_schema(
        operation_description='Deletes a Client object',
        responses={status.HTTP_200_OK: BasicClientSerializer})
    def destroy(self, request, pk=None):
        return super().destroy(request, pk)
