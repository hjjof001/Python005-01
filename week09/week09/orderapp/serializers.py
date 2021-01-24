from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')

    class Meta:
        model = Order
        fields = ['url', 'id', 'product_id', 'buyer', 'status', 'create_time']