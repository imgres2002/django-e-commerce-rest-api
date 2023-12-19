import django_filters

from product.models import Category, Product


class ProductFilter(django_filters.rest_framework.FilterSet):
    """Filers for webcam list"""
    category = django_filters.ModelMultipleChoiceFilter(to_field_name='id', queryset=Category.objects.all())
    product = django_filters.ModelMultipleChoiceFilter(to_field_name='id', queryset=Product.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity', )
