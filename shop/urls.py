from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryList

app_name = ShopConfig.name

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category_list'),

]
