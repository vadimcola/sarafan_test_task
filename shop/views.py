from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.cart import Cart
from shop.models import Category, Product
from shop.paginators import ShopPaginator
from shop.serializers import CategorySerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    """Просмотр списка Категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ShopPaginator
    permission_classes = [AllowAny]


class ProductList(generics.ListAPIView):
    """Просмотр списка Продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ShopPaginator
    permission_classes = [AllowAny]


class CartView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        try:
            product = Product.objects.get(pk=product_id)
            cart = Cart(request)
            cart.add(product, quantity)
            return Response({'detail': 'Товар добавлен в корзину'},
                            status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'detail': 'Товар не существует'},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product = Product.objects.get(pk=product_id)
            cart = Cart(request)
            current_quantity = cart.cart.get(str(product.id), {}).get('quantity', 0)
            if quantity == 0 or quantity < current_quantity:
                cart.remove(product)
            else:
                cart.add(product, quantity - current_quantity)
            return Response({'detail': 'Количество товара обновлено'},
                            status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'detail': 'Товар не найден'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            cart = Cart(request)
            cart.remove(product)
            return Response({'detail': 'Товар удален из корзины'},
                            status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'detail': 'Товар не найден'},
                            status=status.HTTP_404_NOT_FOUND)


class CartDetailView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart_data = list(cart)
        total_quantity = sum(item['quantity'] for item in cart_data)
        total_price = cart.get_total_price()
        return Response({
            'cart': cart_data,
            'total_quantity': total_quantity,
            'order_amount': str(total_price)
        }, status=status.HTTP_200_OK)


class CartClearView(APIView):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return Response({'detail': 'Корзина очищена'})
