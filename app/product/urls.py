from django.urls import path
from rest_framework.routers import SimpleRouter

from product import views

app_name = 'products'

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('matching-product-list/<int:pk>/', views.MatchingProductsListView.as_view(), name='matching-product-list'),
]

router = SimpleRouter()

router.register('categories', views.CategoryViewSet, basename='categories')
router.register('products', views.ProductViewSet, basename='products')
router.register('opinions', views.OpinionViewSet, basename='opinions')

urlpatterns += router.urls

