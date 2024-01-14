from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from product.models import Category, Product, Opinion
from product.serializers import CategorySerializer, ProductSerializer, OpinionSerializer, MatchingProductsSerializer, ProductListSerializer
from product.filters import ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD for category. Only for admin user"""
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD for product. Only for admin user"""
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Product.objects.all()


class ProductPagiantion(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100


class ProductListView(generics.ListAPIView):
    """View for list of products"""
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagiantion
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'price']
    ordering_fields = ['price']


class OpinionViewSet(viewsets.ModelViewSet):
    """CRUD for opinion. Only for admin user"""
    serializer_class = OpinionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Opinion.objects.all()


class MatchingProductsViewSet(viewsets.ModelViewSet):
    serializer_class = MatchingProductsSerializer
    queryset = Product.objects.all()
