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





## Follow System

### Follow a user
POST /auth/follow/{user_id}/   (auth required)

### Unfollow a user
POST /auth/unfollow/{user_id}/

### View followers
GET /auth/{user_id}/followers/

### View following
GET /auth/{user_id}/following/


## Feed

### Get feed
GET /api/feed/   (auth required)

Returns posts from all users the current user is following, ordered by newest first.
