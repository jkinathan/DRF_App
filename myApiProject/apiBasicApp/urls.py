
from django.urls import path
from .views import ArticleList, simple

urlpatterns = [
    
    path('article',ArticleList),
    path('simple',simple.as_view()),
    path('simple/<int:id>',simple.as_view()),


]