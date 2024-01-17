from rest_framework import serializers

from order.models import Order, OrderItem, Voucher


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = [
            'code',
            'price'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'order',
            'product',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = (
            'is_paid',
            'total',
            'code',
            'is_paid',
            'products'
        )


class UserOrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'code', 'products')
