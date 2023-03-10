from django.urls import path
from . import views


urlpatterns = [
    path("transactions", views.list_transactions),
    path("categories", views.list_categories),
]
