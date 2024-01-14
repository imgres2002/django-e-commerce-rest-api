from django.db import models
from product.models import Product
from user.models import User


class Voucher(models.Model):
    code = models.CharField(max_length=10, unique=True, primary_key=True, editable=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.code)


class Cart(models.Model):
    user = models.OneToOneField(User, related_name="user_cart", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    code = models.ForeignKey(Voucher, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        voucher = Voucher.objects.filter(code=self.code)
        if voucher.count() > 0:
            if self.total - voucher.price > 0:
                self.total = self.total - voucher.price
            else:
                self.total = 0
            # voucher.delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_product", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
