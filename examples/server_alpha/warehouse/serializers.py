from django.forms import widgets
from rest_framework import serializers
from warehouse.models import Customer
from warehouse.models import Product
from warehouse.models import Order


class CustomerSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer


class ProductSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
