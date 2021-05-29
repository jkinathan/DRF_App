
from django import urls
from django.urls import path, include
from .views import ArticleList, simple, SimpleGenericsUpdate, SimpleViewSet

# this is for ViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("simpleViewSet",SimpleViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('article',ArticleList),
    path('simple',simple.as_view()),
    path('simple/<int:id>',simple.as_view()),
    # path('simplegenerics',SimpleGenerics.as_view()),
    path('simplegenerics/<int:id>',SimpleGenericsUpdate.as_view())


]