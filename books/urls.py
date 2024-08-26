from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/<str:slug>/', views.BookDetailView.as_view(), name='detailPage'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='commentPage')
]

