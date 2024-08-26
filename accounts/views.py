from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignupForm, DepositForm, BorrowedBookForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import BorrowedBooksModel
from books.models import BookModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from core.views import EmailSend
# Create your views here.
class SignupView(FormView):
    template_name= 'accounts/signup.html'
    form_class= SignupForm
    success_url= reverse_lazy('homePage')

    def form_valid(self, form):
        user= form.save()
        login(self.request, user)
        messages.success(self.request, 'Account Created Successfully.')
        EmailSend(self.request.user, 0, 'Signup', 'accounts/signup_mail.html')
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name= 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('homePage')
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homePage')

class DepositView(LoginRequiredMixin, FormView):
    form_class= DepositForm
    template_name= 'accounts/deposit.html'

    def get_success_url(self):
        return reverse_lazy('homePage')

    def form_valid(self, form):
        amount= form.cleaned_data.get('amount')
        account= self.request.user.account
        account.balance+=amount
        account.save(
            update_fields= ['balance']
        )
        messages.success(self.request, 'Deposit Success')
        EmailSend(self.request.user, amount, 'Deposit', 'accounts/deposit_mail.html')
        return super().form_valid(form)
    
    
    def get_initial(self):
        initial = super().get_initial()
        initial['account'] = self.request.user.account
        return initial
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']= 'Deposit'
        return context

# class ProfileView(TemplateView):
#     template_name= 'accounts/profile.html'

@login_required
def profile(request):
    user_books= BorrowedBooksModel.objects.filter(owner= request.user)
    all_books= []
    all_id=[]
    all_existed_books= BookModel.objects.all()
    for single_book in all_existed_books:
        a= single_book.id
        all_id.append(a)
    # print(all_id)
    for book in user_books:
        if book.borrowed_book in all_id:
            x= BookModel.objects.get(id=book.borrowed_book)
            all_books.append(x)
    return render(request, 'accounts/profile.html', {'data': all_books})

@login_required
def BorrowView(request, id):
    book= BookModel.objects.get(id= id)
    count= BorrowedBooksModel.objects.filter(borrowed_book= id).count()
    if count<1:
        if book.price<=request.user.account.balance:
            request.user.account.balance-=book.price
            request.user.account.save()
            print(request.user.account.balance)
            form= BorrowedBookForm()
            form.instance.owner= request.user
            form.instance.borrowed_book= id
            form.instance.save()
            book.save()
            messages.success(request, 'Borrowed Successfully.')
            EmailSend(request.user, book.price, 'Borrow book', 'accounts/borrow_mail.html')
        else:
            messages.error(request, 'Insufficient Balance.')
    else:
        messages.error(request, 'Already you borrowed this book.')
    return redirect('profilePage')

@login_required
def ReturnView(request, id):
    book= BookModel.objects.get(id= id)
    request.user.account.balance+=book.price
    request.user.account.save()
    print(request.user.account.balance)
    return_book= BorrowedBooksModel.objects.get(borrowed_book=id).delete()
    messages.success(request, 'Returned Successfully')
    EmailSend(request.user, book.price, 'Return book', 'accounts/return_mail.html')
    return redirect('profilePage')

