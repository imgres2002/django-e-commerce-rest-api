from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from cart.models import Cart, CartItem, Voucher
from cart.serializers import CartSerializer, CarItemSerializer, VoucherSerializer


class VoucherViewSet(viewsets.ModelViewSet):
    """CRUD for voucher. Only for admin user"""
    serializer_class = VoucherSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Voucher.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    """CRUD for category. Only for admin user"""
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = Cart.objects.all()

class CarItemViewSet(viewsets.ModelViewSet):
    """CRUD for category. Only for admin user"""
    serializer_class = CarItemSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    queryset = CartItem.objects.all()
