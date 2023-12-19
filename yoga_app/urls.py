from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    # path('', views.home,name='home_youga_app'),
    path('api/v1/registeryoga-user/',views.register_user.as_view()),
    path('api/v1/activate-yoga-user/<uidb64>/<token>/', views.activate_yoga.as_view(),name='activate_yoga_user'),
    path('api/v1/recive-payment/', views.recive_payment.as_view()),
]
