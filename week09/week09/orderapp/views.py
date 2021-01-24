from rest_framework import viewsets, permissions

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