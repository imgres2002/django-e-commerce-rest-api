from rest_framework import serializers

from product.models import Category, Product, Opinion, Voucher


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            # 'parent',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'price',
            'description',
            'quantity',
            'date_added'
        )


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        field = (
            'product',
            'author',
            'title',
            'body',
            'raiting_enum',
            'date_added',
        )


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        field = (
            'code',
            'price',
        )
