from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill#크기조정해주는기능

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 100)], format='JPEG', options={'quality':60})