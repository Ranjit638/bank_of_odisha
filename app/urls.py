from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path("about/", views.about, name="about"),
    path('user_login', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('withdrawl/', views.withdrawal, name='withdrawal'),
    path('balance_check/', views.balance_check, name='balance'),
    path('send/', views.send, name='send'),
    path('deposite', views.deposite, name='deposite'),
    path('display_records/', views.display_records, name='transaction'),
    path('feedback/', views.feedback, name='feedback'),
    
]