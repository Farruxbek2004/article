from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])