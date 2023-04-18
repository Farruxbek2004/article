from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.core.validators import FileExtensionValidator


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
