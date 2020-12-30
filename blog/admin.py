from django.contrib import admin
from .models import Book, Author, AuthorDetail, Publish


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publish)