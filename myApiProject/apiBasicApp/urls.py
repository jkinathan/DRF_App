
from django.urls import path
from .views import ArticleList, simple, SimpleGenerics, SimpleGenericsUpdate

urlpatterns = [
    
    path('article',ArticleList),
    path('simple',simple.as_view()),
    path('simple/<int:id>',simple.as_view()),
    path('simplegenerics',SimpleGenerics.as_view()),
    path('simplegenerics/<int:id>',SimpleGenericsUpdate.as_view())


]