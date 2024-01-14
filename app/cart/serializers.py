from rest_framework import serializers

from cart.models import Cart, CartItem, Voucher


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = [
            'code',
            'price'
        ]


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = (
            'user',
            'total',
            'code'
        )


class CarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
        )
