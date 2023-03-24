from rest_framework import viewsets

from .models import Category, Transaction
from .serializer import (
    CategorySerializer,
    TransactionEditableSerializer,
    TransactionSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action in ["update", "partial_update", "create"]:
            return TransactionEditableSerializer
        return TransactionSerializer
