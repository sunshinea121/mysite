from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    type_choice = ((1, "普通用户"), (2, "VIP"), (3, "SVIP"))
    user_type = models.IntegerField(choices=type_choice, default=1)

    class Meta:
        permissions = (
            (),
        )


class Token(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    token = models.CharField(max_length=128)

    def __str__(self):
        return self.token


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        return self.name
