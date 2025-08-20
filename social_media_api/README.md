## Posts
- List:      GET /api/posts/?page=<n>&search=<q>&ordering=<field|-field>
- Create:    POST /api/posts/   (auth required)
- Retrieve:  GET /api/posts/{id}/
- Update:    PATCH /api/posts/{id}/ (owner only)
- Delete:    DELETE /api/posts/{id}/ (owner only)

Fields:
- id, author {id, username}, title, content, created_at, updated_at, comments_count

## Comments
- List:      GET /api/comments/?page=<n>&search=<q>&ordering=<field|-field>
- Create:    POST /api/comments/ (auth required)
- Retrieve:  GET /api/comments/{id}/
- Update:    PATCH /api/comments/{id}/ (owner only)
- Delete:    DELETE /api/comments/{id}/ (owner only)

Fields:
- id, post, author {id, username}, content, created_at, updated_at
