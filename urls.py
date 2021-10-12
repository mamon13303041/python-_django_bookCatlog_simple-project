from typing import ValuesView
from django.http.request import validate_host
from django.urls import path

from . import views

urlpatterns =[
path('',views.book_view, name='book_view'),
path('book/renew/', views.addbook, name='addbook'),
path('update_books/<str:pk>/', views.updatebooks, name="update_books"),
path('delete_books/<str:pk>/', views.deletebooks, name="delete_books"),
# path('create/', views.create, name='create' ),
# path('addbooks/',views.add_book, name='add_book')

]