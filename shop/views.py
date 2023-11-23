from rest_framework import generics

from shop.models import Category
from shop.paginators import ShopPaginator
from shop.serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    """Просмотр списка Категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ShopPaginator
