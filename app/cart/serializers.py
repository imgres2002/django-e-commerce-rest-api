from rest_framework import serializers

from cart.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'user',
            'total',
        )


class CarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
        )
