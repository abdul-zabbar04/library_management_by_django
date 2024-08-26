from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signupPage'),
    path('login/', views.UserLoginView.as_view(), name='loginPage'),
    path('logout/', views.UserLogoutView.as_view(), name='logoutPage'),
    path('deposit/', views.DepositView.as_view(), name='depositPage'),
    path('profile/', views.profile, name='profilePage'),
    path('borrow/<int:id>/', views.BorrowView, name='borrowPage'),
    path('return/<int:id>/', views.ReturnView, name='returnPage'),
]
