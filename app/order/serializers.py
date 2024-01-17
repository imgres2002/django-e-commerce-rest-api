from rest_framework import serializers

from product.serializers import ProductSerializer
from order.models import Order, OrderItem, Voucher
from product import models


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = [
            'code',
            'price'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all(), source='product',
                                                    write_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='order',
                                                    write_only=True)
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'order',
            'order_id',
            'product_id',
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
