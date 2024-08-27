from django.db import models
from category.models import CategoryModel

# Create your models here.

class BookModel(models.Model):
    title= models.CharField(max_length=150)
    slug= models.SlugField(unique=True, max_length=150, null=True, blank=True)
    image= models.ImageField(upload_to='books/', null=True, blank=True)
    description= models.TextField()
    price= models.DecimalField(max_digits=7, decimal_places=2)
    time_stamp= models.DateTimeField(auto_now_add=True)
    category= models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category' )

    def __str__(self):
        return self.title
    
class CommentModel(models.Model):
    book= models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=50)
    body= models.TextField()
    create_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'comment by {self.name}'