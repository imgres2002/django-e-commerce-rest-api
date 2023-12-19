from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from product.models import Category, Product, Opinion, Voucher
from product.serializers import CategorySerializer, ProductSerializer, OpinionSerializer, VoucherSerializer


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


class OpinionViewSet(viewsets.ModelViewSet):
    """CRUD for opinion. Only for admin user"""
    serializer_class = OpinionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Opinion.objects.all()


class VoucherViewSet(viewsets.ModelViewSet):
    """CRUD for voucher. Only for admin user"""
    serializer_class = VoucherSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Voucher.objects.all()
