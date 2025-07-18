import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
author = Author.objects.filter(name=author_name).first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
else:
    print("Author not found.")

# List all books in a library
library_name = "City Library"
library = Library.objects.filter(name=library_name).first()
if library:
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
else:
    print("Library not found.")

# Retrieve the librarian for a library
if library:
    try:
        librarian = library.librarian
        print(f"Librarian for {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")
