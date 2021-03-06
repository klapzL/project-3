from django.shortcuts import render, get_object_or_404
from .models import Blog, Book

def blogs_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs_list.html', context)

def books_list(request):
    books = Book.objects.all()
    context = { 
        'books': books
    }
    return render(request, 'blogs/books_list.html', context)

def book_details(request, book_id):
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'blogs/book_details.html', context)
