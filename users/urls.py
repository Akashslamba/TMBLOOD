from django.urls import path
from django.conf import settings
from django.contrib.auth import views 
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login')
]
