from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModel, DepositModel, BorrowedBooksModel

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        new_user= super().save(commit=False)
        if commit:
            new_user.save()
            UserModel.objects.create(user= new_user)
        return new_user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':(
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500 '
                )
            })

class DepositForm(forms.ModelForm):
    class Meta:
        model= DepositModel
        fields= ['account','amount']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].disabled= True
        self.fields['account'].widget= forms.HiddenInput()

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model= BorrowedBooksModel
        fields= '__all__'