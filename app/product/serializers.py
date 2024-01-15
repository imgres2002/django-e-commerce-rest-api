from rest_framework import serializers

from product.models import Category, Product, Opinion

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class OpinionSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
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


class ProductSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'price',
            'list_price',
            'description',
            'quantity',
            'date_added',
            'matching_products'
          ]


class ProductListSerializer(serializers.ModelSerializer):
    opinions = OpinionSerializer(read_only=True, many=True, source='opinion_set')
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'description',
            'price',
            'list_price',
            'quantity',
            'opinions'
        ]


class MatchingProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'matching_products'
        ]
