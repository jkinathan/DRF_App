
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from rest_framework.views import APIView
from rest_framework import serializers, generics, viewsets
from rest_framework.parsers import JSONParser
from .models import Article, TestModel
from .serializers import ArticleSerializer, SimpleSerializer
from django.views.decorators.csrf import csrf_exempt

# using seeders
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(Article, 2)

def execute():
    seeder.execute()
    print("Seeding completed")


# Create your views here.
class SimpleViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"


# old class based APIVIEW
class simple(APIView):

    def post(self, request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # above is checking for validations in out serializers
        # creating our data to be inserted from postman to go to the database using objects.create
        # request.data is used to fetch the data being inserted while calling this post method
        
        # newTestContent = TestModel.objects.create(
        #     name = request.data["name"],
        #     description = request.data["description"],
        #     phone = request.data["phone"],
        #     is_alive = request.data["is_alive"],
        #     amount = request.data["amount"]
        # )

        serializer.save()
        # serializer.save() calls the validations and then runs the create function overriden and save it in db
        
        return JsonResponse(
            {
                "data": serializer.data
            })

    def get(self, request):
        content = TestModel.objects.all()

        print(content)

        return JsonResponse({"Get Response": SimpleSerializer(content, many=True).data})
        # many=True is telling your serializer that the data you are dealing with is a list because of the .all() ORM

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None) 
        # validations to check if user passed in an id then None as default if id doesnt exist
        if not model_id:
            return JsonResponse({"error": "Method PUT not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object doesn't Exist Bro!! "})

        # validating our data
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return JsonResponse(
            {
                "data": serializer.data
            })


# Old function based APIView
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