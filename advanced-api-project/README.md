### Book API Endpoints

| Endpoint                  | Method | Description            | Permissions         |
|--------------------------|--------|------------------------|---------------------|
| /api/books/              | GET    | List all books         | Public              |
| /api/books/<id>/         | GET    | Get book by ID         | Public              |
| /api/books/create/       | POST   | Create new book        | Authenticated users |
| /api/books/<id>/update/  | PUT    | Update existing book   | Authenticated users |
| /api/books/<id>/delete/  | DELETE | Delete a book          | Authenticated users |
