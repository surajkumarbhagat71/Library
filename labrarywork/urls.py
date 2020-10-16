from django.urls import path
from .views import *
from  . import  views


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('allbook',AllBooks.as_view(),name="allbook"),
    path('allcategory',AllCategory.as_view(),name="allcategory"),
    path('orderbook',AllOrder.as_view(),name="orderbook"),
    path('order/<int:pk>',Orders.as_view(),name="order"),
    path('addcategory',AddBookCategory.as_view(),name='addcategory'),
    path('addbook',AddBook.as_view(),name='addbook'),
    path('remove_order/<int:pk>',RemoveOrder.as_view(),name="remove_order"),
    path('update_book/<int:pk>',UpdateBook.as_view(),name="update_book"),
    path('search',Search.as_view(),name="serach"),
    path('login', Login.as_view(), name='login'),
    path('logout',Logout.as_view(),name="logout"),


]