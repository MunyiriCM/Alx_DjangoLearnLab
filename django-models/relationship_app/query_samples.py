# relationship_app/query_samples.py

import os
import django

# Set up Django environment
# IMPORTANT: Replace 'django_models.settings' with the actual path to your project's settings file.
# For example, if your project is named 'myproject', it would be 'myproject.settings'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

# Import your models
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- Create Sample Data (or ensure it exists) ---
    print("--- Creating Sample Data (if not already present) ---")
    author1, created = Author.objects.get_or_create(name='Author A')
    author2, created = Author.objects.get_or_create(name='Author B')

    book1, created = Book.objects.get_or_create(title='The Great Adventure', author=author1)
    book2, created = Book.objects.get_or_create(title='Mystery of the Old House', author=author1)
    book3, created = Book.objects.get_or_create(title='Code Like a Pro', author=author2)

    library1, created = Library.objects.get_or_create(name='City Central Library')
    library2, created = Library.objects.get_or_create(name='Suburban Branch')

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2)
    library2.books.add(book2, book3)

    # Create Librarians (OneToOne relationship)
    librarian1, created = Librarian.objects.get_or_create(name='Alice Smith', library=library1)
    librarian2, created = Librarian.objects.get_or_create(name='Bob Johnson', library=library2)
    print("Sample data created/ensured.\n")


    # --- Query all books by a specific author ---
    print("--- Querying all books by a specific author ---")
    try:
        author_to_find = Author.objects.get(name='Author A')
        # Accessing related books using the 'related_name' defined in the Book model
        books_by_author = author_to_find.books.all()
        print(f"Books by {author_to_find.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author 'Author A' not found. Please ensure sample data is created.")

    print("\n--- Listing all books in a library ---")
    try:
        library_to_find = Library.objects.get(name='City Central Library')
        # Accessing related books through the ManyToManyField
        books_in_library = library_to_find.books.all()
        print(f"Books in '{library_to_find.name}':")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library 'City Central Library' not found. Please ensure sample data is created.")

    print("\n--- Retrieving the librarian for a library ---")
    try:
        library_for_librarian = Library.objects.get(name='Suburban Branch')
        # Accessing the related Librarian through the OneToOneField
        librarian_info = library_for_librarian.librarian
        print(f"The librarian for '{library_for_librarian.name}' is: {librarian_info.name}")
    except Library.DoesNotExist:
        print("Library 'Suburban Branch' not found. Please ensure sample data is created.")
    except Librarian.DoesNotExist: # This can occur if a library exists but has no linked librarian
        print(f"No librarian found for '{library_for_librarian.name}'.")

if __name__ == '__main__':
    run_queries()