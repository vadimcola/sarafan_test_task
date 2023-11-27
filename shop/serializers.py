from rest_framework import serializers

from shop.models import Category, Subcategory, Product


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(source='category', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "slug", "image", "subcategory")


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'category', 'subcategory', 'original_image',
                  'small_image', 'large_image')

    def get_category(self, obj):
        return obj.subcategory.category.pk

