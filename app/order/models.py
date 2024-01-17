from django.db import models
from product.models import Product
from django.core.validators import MinLengthValidator
from user.models import User


class Voucher(models.Model):
    code = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5)])
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return '%s - %s' % (self.code, self.price)


class Order(models.Model):
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    code = models.CharField(max_length=10, null=True)
    is_paid = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, through='OrderItem', blank=True)

    def apply_voucher_discount(self):
        voucher = Voucher.objects.filter(code=self.code)
        if voucher.count() > 0:
            if self.total - voucher.price > 0:
                self.total = self.total - voucher.price
            else:
                self.total = 0
            if self.is_paid:
                voucher.delete()

    def calculate_order_total(self):
        order_item = OrderItem.objects.filter(order=self.id)
        if order_item.count() > 0:
            for order_item in self.products.all():
                self.total += order_item.quantity * order_item.product.price

    def quantity_decrease(self):
        if self.is_paid:
            order_item = OrderItem.objects.filter(order=self.id)
            if order_item.count() > 0:
                for order_item in self.products.all():
                    if order_item.product.quantity >= order_item.quantity:
                        order_item.product.quantity -= order_item.quantity

    def save(self, *args, **kwargs):
        self.calculate_order_total()
        self.apply_voucher_discount()
        self.quantity_decrease()

        super().save(*args, **kwargs)


    def __str__(self):
        return '%s - %s' % (self.total, self.is_paid)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_item", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, related_name="order_product", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
