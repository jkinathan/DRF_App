from django.contrib import admin
from .models import Article, TestModel, ModelX

# Register your models here.
admin.site.register((Article,TestModel,ModelX))
# admin.site.register(TestModel)
# admin.site.register(ModelX)
