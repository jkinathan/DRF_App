
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Article, TestModel
from .serializers import ArticleSerializer, SimpleSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class simple(APIView):

    def post(self, request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # above is checking for validations in out serializers
        # creating our data to be inserted from postman to go to the database using objects.create
        # request.data is used to fetch the data being inserted while calling this post method
        newTestContent = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone = request.data["phone"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        
        return JsonResponse(
            {
                "data": SimpleSerializer(newTestContent).data
            })

    def get(self, request):
        content = TestModel.objects.all()

        print(content)

        return JsonResponse({"Get Response": SimpleSerializer(content, many=True).data})
        # many=True is telling your serializer that the data you are dealing with is a list because of the .all() ORM





@csrf_exempt
def ArticleList(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)