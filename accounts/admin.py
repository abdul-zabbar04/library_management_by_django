from django.contrib import admin
from .models import UserModel, BorrowedBooksModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(BorrowedBooksModel)
