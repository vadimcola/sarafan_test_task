from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import Product


@receiver(post_save, sender=Product)
def make_image_thumbnails(sender, instance, **kwargs):
    if instance.original_image:
        # Обработка изображения малого размера
        small_image = Image.open(instance.original_image.path)
        small_image.thumbnail((100, 100))
        small_image.save(instance.small_image.path)

        # Обработка изображения большого размера
        large_image = Image.open(instance.original_image.path)
        large_image.thumbnail((800, 800))
        large_image.save(instance.large_image.path)
