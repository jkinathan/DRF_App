from rest_framework import fields, serializers
from .models import Article


# class SimpleObject():
#     def __str__(self, name):
#         self.name = name

class SimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    phone = serializers.IntegerField()
    is_alive = serializers.BooleanField()
    amount = serializers.CharField()
    slug = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


# def run_data():
#     simpleVar = SimpleObject("Jordan")
#     simpleVarSerializer = SimpleObjectSerializer(simpleVar)

#     print(simpleVarSerializer.data)
# for Serializer class
# class ArticleSerializer(serializers.Serializer):
#     title =  serializers.CharField(max_length=50)
#     author = serializers.CharField(max_length=100)
#     email =  serializers.EmailField(max_length=50)
#     date =   serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author',instance.author)
#         instance.email = validated_data.get('email',instance.email)
#         instance.date = validated_data.get('date',instance.date)

#         instance.save()

#         return instance

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author','email','date']