from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from shop.models import Product


@receiver(post_save, sender=Product)
def create_product_images(sender, instance, created, **kwargs):
    if created:
        # Открывает оригинальное изображение
        original_image = Image.open(instance.image_original.path)

        # Создает и сохраняет миниатюры разных размеров
        small_image = original_image.resize((200, 200))
        small_image.save(instance.image_small.path)

        medium_image = original_image.resize((300, 300))
        medium_image.save(instance.image_medium.path)

        large_image = original_image.resize((500, 500))
        large_image.save(instance.image_large.path)
