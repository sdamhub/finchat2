from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('welcome', views.welcome, name='welcome'),
    path('welcome_next', views.welcome_next, name='welcome_next'),
     path('customer_care', views.customer_care, name='customer_care'),

]