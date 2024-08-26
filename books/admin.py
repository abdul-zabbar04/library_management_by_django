from django.contrib import admin
from .models import BookModel, CommentModel

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}
    list_display=['title', 'slug']
admin.site.register(BookModel, BookAdmin)
admin.site.register(CommentModel)