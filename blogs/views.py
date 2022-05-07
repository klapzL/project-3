from django.shortcuts import render
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