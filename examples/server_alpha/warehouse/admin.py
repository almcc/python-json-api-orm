from django.contrib import admin
from warehouse.models import Customer
from warehouse.models import Product
from warehouse.models import Order

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)