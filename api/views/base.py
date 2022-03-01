from abc import ABCMeta, abstractmethod

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BaseViewSet(viewsets.ViewSet, metaclass=ABCMeta):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    @abstractmethod
    def serializer(self):
        pass

    @staticmethod
    def _save(serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def list(self, request):
        items = self.model.objects.all()
        serializer = self.serializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer(data=request.data)
        data = self._save(serializer)
        return Response(data)

    def update(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(
            item, data=request.data)
        data = self._save(serializer)
        return Response(data)

    def partial_update(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(
            item, data=request.data, partial=True)
        data = self._save(serializer)
        return Response(data)

    def destroy(self, request, pk=None):
        item = get_object_or_404(self.model, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
