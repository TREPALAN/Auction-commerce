from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('auction/<int:pk>/', views.AuctionView.as_view(), name ='auction'),
    path('register/', views.CreateUserView.as_view(), name ='register'),
    path('watchlist/', views.WatchlistView.as_view(), name ='watchlist'),
    path('getwatchlist/', views.GetWatchlistView.as_view(), name ='getwatchlist'),
    path('AddComment/<int:pk>/', views.CommentView.as_view(), name ='comments'),
    path('categories/', views.CategoryView.as_view(), name ='categories'),
    path('newAuction/', views.NewAuctionView.as_view(), name ='new'),
    path('DeleteAuction/<int:pk>/', views.DeleteAuctionView.as_view(), name ='delete'),
    path('bid/<int:pk>/', views.BidView.as_view(), name ='bid'),
    
]