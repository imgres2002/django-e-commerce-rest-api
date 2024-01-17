from django.urls import path
from rest_framework.routers import SimpleRouter

from order import views

app_name = 'order'

urlpatterns = [
    path('orders/', views.UserOrderViewSet.as_view({'get': 'list'}), name='order-list'),
    path('orders/new/', views.CreateOrderViewSet.as_view({'post': 'create'}), name='create-new'),
    path('orders/<int:pk>/', views.UpdateOrderViewSet.as_view({'get': 'retrieve'}), name='order-detail'),
    path('orders/<int:pk>/edit/', views.UpdateOrderViewSet.as_view({'put': 'update'}), name='order-edit'),
    path('orders/<int:pk>/delete/', views.UpdateOrderViewSet.as_view({'delete': 'destroy'}), name='order-delete'),
    path('orders/<int:pk>/pay/', views.MarkOrderAsPaidView.as_view(), name='order-pay'),
]
router = SimpleRouter()

router.register('vouchers', views.VoucherViewSet, basename='vouchers')
router.register('orders-admin', views.OrderViewSet, basename='orders-admin')
router.register('order_items', views.OrderItemViewSet, basename='order_items')

urlpatterns += router.urls
