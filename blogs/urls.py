from django.urls import path
from .views import blogs_list, books_list, book_details

urlpatterns = [
    path('blogs_list/', blogs_list, name='blogs_list'),
    path('books_list/', books_list, name='books_list'),
    path('books/<int:book_id>', book_details, name='book_details'),
]