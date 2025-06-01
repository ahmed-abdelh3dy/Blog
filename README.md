# 📰 Blog API with Django & JWT

This is a RESTful Blog API built using Django and Django REST Framework (DRF).  
It includes full JWT authentication, and allows users to create posts and comment on them.

---

## 🚀 Features

- User Registration & Login with JWT
- Create, Read, Update, Delete (CRUD) for Posts
- Add and view Comments on Posts
- Authenticated & permission-based API access
- Clean RESTful endpoints using Django REST Framework

---

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for secure authentication.  
Implemented using `djangorestframework-simplejwt`.

- `POST /api/register — Register a new user  
- `POST /api/login — Get JWT token (login)

- 
📌 API Endpoints
📂 Posts
Method	Endpoint	Description
GET	/api/post	Retrieve all blog posts
POST	/api/post	Create a new post (requires auth)
GET	/api/post/status	Get post statuses
GET	/api/post/<id>	Retrieve a single post by ID
PUT	/api/post/<id>	Update a post (requires auth)
DELETE	/api/post/<id>	Delete a post (requires auth)

💬 Comments
Method	Endpoint	Description
GET	/api/comment	Retrieve all comments
POST	/api/comment	Add a comment (requires auth)
GET	/api/comment/<id>	Retrieve a single comment by ID
PUT	/api/comment/<id>	Update a comment (requires auth)
DELETE	/api/comment/<id>	Delete a comment (requires auth)

