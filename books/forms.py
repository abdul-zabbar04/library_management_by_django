from .models import CommentModel
from django.forms import ModelForm
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model= CommentModel
        fields=['book', 'name', 'body']
    def __init__(self, book_id = None, user_name= None, *args, **kwargs):
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
        self.fields['book'].disabled= True
        self.fields['book'].widget= forms.HiddenInput()
        self.fields['name'].disabled= True
        self.fields['name'].widget= forms.HiddenInput()
        if book_id and user_name:
            self.fields['book'].initial= book_id
            self.fields['name'].initial= user_name
  