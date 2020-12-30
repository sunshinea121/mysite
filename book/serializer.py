from django.views import View
from .models import Publish
import json
from rest_framework import serializers
from .models import Book

class PublishSerializers(serializers.Serializer):
    """
    为QuerySet做序列化
    """
    name = serializers.CharField()
    email = serializers.CharField()


class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    pub_date = serializers.DateField()
    publish = serializers.CharField(source="publish.name")
    # authors = serializers.CharField(source="authors.all")
    authors = serializers.SerializerMethodField()

    def get_authors(self, obj):
        temp = []
        for author in obj.authors.all():
            temp.append(author.name)
        return temp


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        # 帮忙转换没有自己写的字段
        model = Book
        fields = "__all__"

    publish = serializers.CharField(source="publish.pk")
    # authors = serializers.SerializerMethodField()

    # def get_authors(self, obj):
    #     temp = []
    #     for author in obj.authors.all():
    #         temp.append(author.name)
    #     return temp
    def create(self, validated_data):
        print(validated_data)
        authors = validated_data['authors']
        # 添加记录
        book_obj = Book.objects.create(title=validated_data['title'], price=validated_data['price'],
                                       pub_date=validated_data['pub_date'], publish_id=validated_data['publish']['pk'])
        book_obj.authors.add(*authors)
        return book_obj
