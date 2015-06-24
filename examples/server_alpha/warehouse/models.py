from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)

class Order(models.Model):
    name = models.CharField(max_length=30)
    total = models.IntegerField()
    customer = models.ForeignKey(Customer)
    products = models.ManyToManyField(Product)
    paid = models.BooleanField()

    def __str__(self):
        return "{}".format(self.name)
