from django.urls import path
from rest_framework.routers import SimpleRouter

from cart import views

app_name = 'cart'

router = SimpleRouter()

router.register('vouchers', views.VoucherViewSet, basename='vouchers')
router.register('cart', views.CartViewSet, basename='cart')
router.register('cart-item', views.CarItemViewSet, basename='cart-item')

urlpatterns = router.urls
