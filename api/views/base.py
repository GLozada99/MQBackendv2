from abc import ABCMeta, abstractmethod

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from extras.decorators import method_permission_classes


class BaseViewSet(viewsets.ViewSet, metaclass=ABCMeta):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    @abstractmethod
    def reading_serializer(self):
        pass

    @property
    @abstractmethod
    def creating_serializer(self):
        pass

    @staticmethod
    def _save(serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def list(self, request):
        items = self.model.objects.all()
        serializer = self.reading_serializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.reading_serializer(item)
        return Response(serializer.data)

    @method_permission_classes([permissions.IsAdminUser])
    def create(self, request):
        serializer = self.creating_serializer(data=request.data)
        data = self._save(serializer)
        return Response(data)

    @method_permission_classes([permissions.IsAdminUser])
    def update(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.creating_serializer(
            item, data=request.data)
        data = self._save(serializer)
        return Response(data)

    @method_permission_classes([permissions.IsAdminUser])
    def partial_update(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.creating_serializer(
            item, data=request.data, partial=True)
        data = self._save(serializer)
        return Response(data)

    @method_permission_classes([permissions.IsAdminUser])
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
