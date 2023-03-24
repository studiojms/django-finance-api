from rest_framework import serializers

from .models import Category, Transaction


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    parent_category = SimpleCategorySerializer(read_only=True)
    subcategories = SimpleCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "parent_category", "subcategories")


class TransactionSerializer(serializers.ModelSerializer):
    category = SimpleCategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ("id", "date", "amount", "description", "type", "category")


class TransactionEditableSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ("id", "date", "amount", "description", "type", "category")
