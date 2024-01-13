from rest_framework import serializers

from product.models import Category, Product, Opinion, Voucher

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')

    class Meta:
        model = Product
        fields = ['id',
                  'category',
                  'name',
                  'price',
                  'list_price',
                  'description',
                  'quantity',
                  'date_added',
                  'matching_products'
                  ]


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = [
            'product',
            'author',
            'title',
            'body',
            'raiting_enum',
            'date_added'
        ]


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = [
            'code',
            'price'
        ]

class MatchingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'matching_products'
        ]