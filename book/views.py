from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from .serializer import PublishSerializers, BookSerializers, BookModelSerializers
from .models import Publish, Book
import json
from rest_framework import status
# class PublishView(APIView):
#     def get(self, request):
#         print('request.data', request.data)
#         print('request.data type', type(request.data))
#         print('request._requet.GET', request._request.GET)
#         print('request.GET', request.GET)
#
#         return HttpResponse('123')
#
#     def post(self, request):
#         # 原生request支持的操作
#         # print('post', request.POST)
#         # print('body', request.body)
#         # print(type(request))
#         from django.core.handlers.wsgi import WSGIRequest
#         # 新的request支持的操作
#         print("request.data", request.data)
#         print("request.data type", type(request.data))
#
#         return HttpResponse('POST')

from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    # 默认煤业显示数据的条数
    page_size = 2
    # 获取URL参数中设置的煤业显示数据条数
    page_size_query_param = 'size'
    # 获取url传参中传入的页码key
    page_query_param = 'page'
    # 最大支持的煤业显示的数据条数（进行显示/book/?page=1&size=100)
    max_page_size = 5


class PublishView(View):
    pagination_class = MyPageNumberPagination  # 在视图中使用pagination_class属性调用该自定义类

    def get(self, request):
        # 方式4：
        publish_list = Publish.objects.all()
        ret = PublishSerializers(publish_list, many=True)  # 描述是model对象还是QuerySet  True：queryset
        return HttpResponse(json.dumps(ret))

    def post(self, request):
        pass


# class BookView(APIView):
#     def get(self, request):
#         book_list = Book.objects.all()
#         bs = BookSerializers(book_list, many=True)  # 序列化结果
#
#         # return HttpResponse(bs.data)
#         return Response(bs.data)
#
#     def post(self):
#         pass


class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        bs = BookModelSerializers(book_list, many=True)  # 序列化结果
        return Response(bs.data)

    def post(self, request):
        # POST请求的数据
        bs = BookModelSerializers(data=request.data)
        if bs.is_valid():   # 验证数据是否合格
            print(bs.validated_data)
            bs.save()   # create方法
            return Response(bs.data)    # 当前添加的数据
        else:
            return Response(bs.errors)


class BookDetailView(APIView):
    def get(self, request, id):
        book_obj = Book.objects.get(pk=id)
        print(book_obj)
        bs = BookModelSerializers(book_obj)
        # 查看单条数据
        return Response(bs.data)

    def put(self, request, id):
        book_obj = Book.objects.get(pk=id)
        # 做更新操作
        bs = BookModelSerializers(book_obj, data=request.data)
        # 校验数据是否有问题
        if bs.is_valid():
            # 模型序列化的update方法
            bs.save()
            # 查看更新的数据
            return Response(bs.data)
        else:
            return HttpResponse(bs.errors)

    def delete(self, request, book_id):
        Book.objects.get(pk=book_id).delete()
        return Response(status=status.HTTP_201_CREATED)

