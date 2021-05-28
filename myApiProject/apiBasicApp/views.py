
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Article, TestModel
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class simple(APIView):

    def post(self, request):
        
        # creating our data to be inserted from postman to go to the database using objects.create
        # request.data is used to fetch the data being inserted while calling this post method
        newTestContent = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone = request.data["phone"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        
            
        print(newTestContent)

        return JsonResponse(
            {
                "data": model_to_dict(newTestContent)
            })

    def get(self, request):
        content = TestModel.objects.all().values()

        print(content)

        return JsonResponse({"Get Response": list(content)})





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