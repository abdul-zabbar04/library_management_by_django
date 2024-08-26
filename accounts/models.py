from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    balance= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self) -> str:
        return f'{self.user.username}'

class DepositModel(models.Model):
    account= models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='transactions')
    amount= models.DecimalField(max_digits=12, decimal_places=2)
    timestamp= models.DateTimeField(auto_now_add=True)

class BorrowedBooksModel(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_book')
    borrowed_book= models.IntegerField(null=True, blank=True)