from django.contrib import admin
from .models import Book, User, Author, Token, Publish

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Token)
admin.site.register(Publish)
