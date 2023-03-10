from rest_framework import serializers
from .models import Category, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # TODO how to calculate amount based on type?
        fields = ("date", "amount", "description", "type", "category")


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ("name", "parent_category")
