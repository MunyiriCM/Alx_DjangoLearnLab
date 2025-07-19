from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Create your views here.
from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to show library details and books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


def list_books(request):
    books = Book.objects.select_related('author').all()
