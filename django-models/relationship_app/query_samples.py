# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
george = Author.objects.get(name="George Orwell")
books_by_george = Book.objects.filter(author=george)
print("Books by George Orwell:", list(books_by_george))

# 2. List all books in a specific library
central_library = Library.objects.get(name="Central Library")
books_in_library = central_library.books.all()
print("Books in Central Library:", list(books_in_library))

# 3. Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=central_library)
print("Librarian for Central Library:", librarian.name)
