from django.contrib import admin

# Register your models here.
from home.models import ArticleCategory

# 注册模型
admin.site.register(ArticleCategory)