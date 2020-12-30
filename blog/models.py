from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    # state = models.BooleanField()
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2) # 浮点型，最大位8位，小数点2位
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    """
    出版社表
    """
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    # email = models.EmailField

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    作者表
    与AuthorDetail建立一对一关系，任意一边都可以
    to="AuthorDetail",加引号不会因为位置关系找不到AuthorDetail
    """
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=30)
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    """
    作者详情表
    """
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)
