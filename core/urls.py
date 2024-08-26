from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='homePage'),
    path('category/<str:slug>/', HomeView.as_view(), name='CateWisePage'),

]
