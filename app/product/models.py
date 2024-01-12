from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    list_price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


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
    code = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.code)
