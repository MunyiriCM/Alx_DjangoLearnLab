from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    # 1. Fetch the book instance or return 404 if not found
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        # 2. Bind the submitted data to the form instance
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            # 3. Save the updated book
            form.save()
            # 4. Redirect to the book list or success page
            return redirect('book_list')
    else:
        # If GET request, render the form with the book data
        form = BookForm(instance=book)

    # 5. Render the edit form template
    return render(request, 'bookshelf/book_form.html', {'form': form})
