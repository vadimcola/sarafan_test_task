from rest_framework import serializers

from shop.models import Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(source='category', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "slug", "image", "subcategory")

