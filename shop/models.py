from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Наименование категории')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True,
                              verbose_name="Изображение")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Наименование подкатегории')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='subcategory/%Y/%m/%d', blank=True,
                              verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category', verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'


class Product(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Наименование продукта')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True,
                              verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена продукта')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    related_name='subcategory', verbose_name='Подкатегория')
    image_original = models.ImageField(upload_to='product_images/original/')
    image_small = models.ImageField(upload_to='product_images/small/', **NULLABLE)
    image_medium = models.ImageField(upload_to='product_images/medium/', **NULLABLE)
    image_large = models.ImageField(upload_to='product_images/large/', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



