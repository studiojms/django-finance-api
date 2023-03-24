from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Account, Category, Transaction
from .serializer import (
    AccountSerializer,
    CategorySerializer,
    TransactionEditableSerializer,
    TransactionSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action in ["update", "partial_update", "create"]:
            return TransactionEditableSerializer
        return TransactionSerializer
