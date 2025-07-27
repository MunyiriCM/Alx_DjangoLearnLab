from django import forms
from relationship_app.models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # adjust fields as per your model

