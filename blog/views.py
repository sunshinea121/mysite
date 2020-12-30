from django.shortcuts import render, HttpResponse
from blog.models import Book


def index(request):
    # 添加表记录：
    # 方式一：
    book_obj = Book(id=1, title="python红宝书", price=100, pub_date="2012-12-12", publish="人民出版社")  # pub_date格式固定
    book_obj.save()

    # 方式二：
    # create方法的返回值book_obj就是当前生成的对象记录
    # id不用传因为是自增的
    book_obj = Book.objects.create(title="php宝典", price=100, pub_date="2013-2-12", publish="人民出版社")

    book_obj.authors.name(pk=1)
    print(book_obj.title)
    print(book_obj.price)
    print(book_obj.pub_date)

    return HttpResponse("OK")