from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import BookModel, CommentModel
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookDetailView(DetailView):
    model= BookModel
    template_name= 'books/detail.html'
    query_pk_and_slug= True 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        comments= CommentModel.objects.filter(book= pk)
        context['comments']= comments
        return context

    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = CommentModel
    form_class= CommentForm
    template_name= 'books/comment.html'
    success_url= reverse_lazy('profilePage')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs= super().get_form_kwargs(*args, **kwargs)
        kwargs['book_id']= self.kwargs.get('pk')
        kwargs['user_name']= self.request.user.first_name +" "+ self.request.user.last_name
        return kwargs
    

