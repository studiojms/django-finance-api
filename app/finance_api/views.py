from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import CategorySerializer, TransactionSerializer

from .models import Category, Transaction


@api_view(["GET"])
def list_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
