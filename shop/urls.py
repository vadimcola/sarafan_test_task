from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryList, ProductList, CartView, CartDetailView, CartClearView

app_name = ShopConfig.name

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category_list'),
    path('product/', ProductList.as_view(), name='product_list'),
    path('cart/', CartView.as_view(), name='cart-manage'),  # Добавление/изменение/удаление
    path('cart/details/', CartDetailView.as_view(), name='cart-detail'),  # Вывод содержимого
    path('cart/clear/', CartClearView.as_view(), name='cart-clear'),  # Очистка корзины
]
