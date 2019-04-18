from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image

class Suit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Diceroll(models.Model):
    pair = models.CharField(max_length=10)

    def __str__(self):
        return self.pair

class Card(models.Model):
    name = models.CharField(max_length=200)
    suit = models.ForeignKey(Suit, on_delete=models.CASCADE)
    diceroll = models.ForeignKey(Diceroll, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'imgs/', default = 'imgs/dummy.jpg', width_field='image_width', height_field='image_height')
    image_width = models.PositiveIntegerField(default = "360")
    image_height = models.PositiveIntegerField(default = "528")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
