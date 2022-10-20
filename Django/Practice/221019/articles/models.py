from django.db import models
from accounts.models import User

class Article(models.Model):
    # 글 작성자
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()


