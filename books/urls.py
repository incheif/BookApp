from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Welcome page!
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('books/', views.book_list, name='book_list'),  # 👈 moved book list here
]