# Flask Blog with Authentication

A clean, responsive blog platform built with Flask and SQLite authentication.

## Features

- User authentication system (signup, login, logout)
- User profile pages
- Contact form with email integration
- Dynamic blog content from API
- Responsive design using Bootstrap 5
- Flash message notifications
- Secure password storage using hashing

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-blog.git
   cd flask-blog
   ```

2. Install dependencies:
   ```
   pip install flask werkzeug requests
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the blog at:
   ```
   http://localhost:7000
   ```

## Project Structure

```
flask-blog/
├── app.py                 # Main Flask application
├── blog.db                # SQLite database (created automatically)
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── assets/
└── templates/             # HTML templates
    ├── base.html          # Base template with layout structure
    ├── index.html         # Homepage with blog posts
    ├── about.html         # About page
    ├── contact.html       # Contact form
    ├── post.html          # Individual blog post
    ├── login.html         # Login form
    ├── signup.html        # Signup form
    ├── profile.html       # User profile page
    └── footer.html        # Footer include
```

## Authentication System

The blog uses a SQLite database with secure password hashing through Werkzeug's security features:

- User information is stored in the `users` table
- Passwords are hashed before storage
- Session management for logged-in users
- Protection against duplicate emails
- Flash messages for user feedback

## Template Structure

Templates follow a hierarchical structure:

- `base.html`: Contains the basic HTML structure, navigation, and footer includes
- Other templates extend `base.html` and override content blocks

## Configuration

To configure the application:

1. Set a secure secret key in `app.py`:
   ```python
   app.secret_key = "your-random-secure-key"
   ```

2. Update email settings for the contact form in `app.py`:
   ```python
   my_email = "your-email@gmail.com"
   my_password = "your-app-password"
   ```

## API Integration

Blog posts are fetched from an external API endpoint. To change the data source:

1. Update the `API_ENDPOINT` variable in `app.py`:
   ```python
   API_ENDPOINT = "your-api-endpoint"
   ```

## Security Notes

- Passwords are securely hashed using Werkzeug's `generate_password_hash`
- Email uniqueness is enforced at the database level
- Session management for tracking logged-in users
- Protection against SQL injection using parameterized queries

## Future Enhancements

- Email verification for new accounts
- Password reset functionality
- User roles/permissions
- Comment system for blog posts
- User profile image uploads

## License

[MIT License](LICENSE)
