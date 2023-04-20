from django.contrib import admin
from .models import Article, ArticleVideo


# Register your models here.


class ArticleVideoInline(admin.TabularInline):
    model = ArticleVideo
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleVideoInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ArticleVideo)
class ArticleVideoAdmin(admin.ModelAdmin):
    list_display = ['article', 'video']
