from django.urls import path
from rest_framework.routers import SimpleRouter

from product import views

app_name = 'products'

router = SimpleRouter()

router.register('categories', views.CategoryViewSet, basename='categories')
router.register('products', views.ProductViewSet, basename='products')
router.register('opinions', views.OpinionViewSet, basename='opinions')
router.register('vouchers', views.VoucherViewSet, basename='vouchers')

urlpatterns = router.urls
