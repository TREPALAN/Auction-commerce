from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Token routes
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('home/', views.HomeView.as_view(), name ='home'),

    # Api routes
    path('Getauctions/', views.auctions, name='auctions'),
    path('getUser/', views.getUser, name='getUser'),
]