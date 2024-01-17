from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from order.models import Order, OrderItem, Voucher
from order.serializers import OrderSerializer, UserOrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user.id)


class UpdateOrderViewSet(viewsets.ModelViewSet):
    serializer_class = UserOrderSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user.id, is_paid=False)


class CreateOrderViewSet(viewsets.ModelViewSet):
    serializer_class = UserOrderSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

class MarkOrderAsPaidView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_paid:
            return Response({"detail": "Order is already paid."}, status=status.HTTP_400_BAD_REQUEST)

        instance.is_paid = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
