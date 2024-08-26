from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import BookModel
from category.models import CategoryModel
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

class HomeView(TemplateView):
    template_name= 'core/home.html'

    def get_context_data(self, slug=None, **kwargs):
        context= super().get_context_data(**kwargs)
        context['books']= BookModel.objects.all()
        context['categories']= CategoryModel.objects.all()
        if slug is not None:
            print(slug)
            category= CategoryModel.objects.get(slug= slug)
            context['books']= BookModel.objects.filter(category= category)

        return context

def EmailSend(user, amount, subject, message_tem):
    message = render_to_string(message_tem, {
        'user': user,
        'amount': amount,
    })
    send_mail= EmailMultiAlternatives(subject, '', to=[user.email])
    send_mail.attach_alternative(message, 'text/html')
    send_mail.send()
