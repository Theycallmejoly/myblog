# Blog Application

This is a Django-based blog application that allows users to create, update, and delete blog posts. It also supports user registration and authentication.

## Features

- User registration and authentication
- Create, read, update, and delete (CRUD) operations for blog posts
- User-specific post management
- Post listing and detail views
- User authentication for post creation, update, and deletion

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the database migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Home

The home page lists all blog posts ordered by their creation date.

### User Posts

Authenticated users can view their own posts by navigating to the `my_posts` page.

### Create Post

Authenticated users can create new posts by navigating to the `create_post` page.

### Update Post

Authenticated users can update their own posts by navigating to the `update_post` page for a specific post.

### Delete Post

Authenticated users can delete their own posts by navigating to the `delete_post` page for a specific post.

### Post List

All posts can be viewed in a list format on the `post_list` page.

### Post Detail

Details of a specific post can be viewed on the `post_detail` page.

### Sign Up

New users can register on the `signup` page.

## Code Overview

### Views

- `home`: Fetches and displays all posts ordered by creation date.
- `my_posts`: Fetches and displays posts created by the authenticated user.
- `update_post`: Allows authenticated users to update their own posts.
- `delete_post`: Allows authenticated users to delete their own posts.
- `post_list`: Fetches and displays all posts.
- `post_detail`: Displays details of a specific post.
- `create_post`: Allows authenticated users to create a new post.
- `signup`: Handles user registration.

### Forms

- `PostForm`: Form for creating and updating posts.
- `SignUpForm`: Form for user registration.

### Models

- `Post`: Model representing a blog post with fields for title, content, author, and timestamps.

## Templates

Templates are located in the `templates/blog` directory and include:

- `home.html`: Displays all posts on the home page.
- `my_posts.html`: Displays posts created by the authenticated user.
- `post_form.html`: Form for creating and updating posts.
- `create_post.html`: Form for creating a new post.
- `post_list.html`: Displays a list of all posts.
- `post_detail.html`: Displays details of a specific post.
- `signup.html`: Form for user registration.


## Contact

For questions or comments, please contact [theycallmejoly@outlook.com].

---

