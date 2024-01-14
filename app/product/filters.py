import django_filters

from product.models import Product


class ProductFilter(django_filters.rest_framework.FilterSet):
    """Filers for product list"""
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
            'description': ['icontains'],
            'price': ['gt', 'lt']
        }
