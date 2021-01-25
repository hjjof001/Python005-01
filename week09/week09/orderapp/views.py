from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from orderapp.models import Order
from orderapp.permissions import IsBuyerOrReadOnly
from orderapp.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsBuyerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def cancel(self, request, pk, *args, **kwargs):
        try:
            order = Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404

        if order.status == 2:
            return Response(status=status.HTTP_200_OK)

        order.status = 2
        order.save()
        return Response(status=status.HTTP_201_CREATED)