from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryList, ProductList

app_name = ShopConfig.name

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category_list'),
    path('product/', ProductList.as_view(), name='product_list'),
]
