from django.db import models


class Flat(models.Model):
    title = models.TextField('Описание')
    flat = models.TextField('Описание')
    image = models.ImageField(upload_to='flat_photo', blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'