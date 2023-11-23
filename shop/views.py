from rest_framework import generics

from shop.models import Category, Product
from shop.paginators import ShopPaginator
from shop.serializers import CategorySerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    """Просмотр списка Категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ShopPaginator


class ProductList(generics.ListAPIView):
    """Просмотр списка Продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ShopPaginator
