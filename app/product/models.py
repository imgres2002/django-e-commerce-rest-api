from django.db import models
from user.models import User
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10,null=True)
    list_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    description = models.TextField(null=True)
    quantity = models.IntegerField(default=1, null=True)
    date_added = models.DateField(auto_now=True)
    matching_products = models.ManyToManyField('self', blank=True,symmetrical=True)

    def save(self, *args, **kwargs):
        if self.price < self.list_price * Decimal.from_float(0.9):
            Outlet.objects.update_or_create(product=self)
        else:
            object = Outlet.objects.filter(product=self)
            if object.count() > 0:
                Outlet.objects.filter(product=self).delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Outlet(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)


class Opinion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    body = models.TextField()


    class RaitingEnum(models.IntegerChoices):
        ZERO = 0,
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,

    raiting_enum = models.IntegerField(choices=RaitingEnum.choices, default=RaitingEnum.FIVE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.author, self.title, self.body)


class Voucher(models.Model):
    code = models.CharField(max_length=10, unique=True, primary_key=True, editable=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.code)
