# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    image_description = models.TextField(blank=True, null=True)

    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)

    #    if self.image and not self.image_description:
    #        description = generate_image_description(self.image.path)
    #        self.image_description = description
    #        super().save(update_fields=['image_description'])

