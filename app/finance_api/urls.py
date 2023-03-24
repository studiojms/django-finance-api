from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("transactions", views.TransactionViewSet, basename="transactions")

urlpatterns = [
    path("", include(router.urls)),
]
