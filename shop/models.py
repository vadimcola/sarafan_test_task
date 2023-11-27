from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Наименование категории')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/', blank=True,
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
    image = models.ImageField(upload_to='subcategory/', blank=True,
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
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена продукта')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    related_name='subcategory', verbose_name='Подкатегория')
    original_image = models.ImageField(upload_to='product_images/original/', blank=True,
                                       verbose_name="Изображение")
    small_image = models.ImageField(upload_to='product_images/small/', blank=True,
                                    verbose_name="Маленькое изображение")
    large_image = models.ImageField(upload_to='product_images/large/', blank=True,
                                    verbose_name="Большое изображение")

    def __str__(self):
        return f'{self.name}'

    def to_json(self):
        """
        Функция возвращает имя продукта, функция используется
        в корзине покупок
        """
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


