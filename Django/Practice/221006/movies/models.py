from django.db import models

class Movie(models.Model):
    title = models.TextField()
    summary = models.TextField()
    running_time = models.IntegerField()
