from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    thumbnail = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality': 90},
    )

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    