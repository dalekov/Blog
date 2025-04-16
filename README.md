
# Flask Blog with Authentication

A clean, responsive blog platform built with Flask and SQLite authentication. The application allows users to create, read, update, and delete blog posts, along with a robust authentication system to manage user sessions and interactions.

## Features

- **User Authentication System**: Includes signup, login, and logout functionality.
- **User Profile Pages**: Each user has a personalized profile page.
- **Contact Form with Email Integration**: A functional contact form that sends emails to the admin.
- **Dynamic Blog Content from API**: Fetch blog posts dynamically from an external API endpoint.
- **Responsive Design**: The platform uses Bootstrap 5 to ensure it's mobile-friendly.
- **Flash Message Notifications**: Alerts to notify users of important actions (e.g., successful login, error messages).
- **Secure Password Storage**: Passwords are securely hashed using Werkzeug’s `generate_password_hash`.

## Installation

Follow these steps to get the application up and running:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
```

### 2. Install Dependencies

The application relies on a few Python libraries. Install them using `pip`:

```bash
pip install flask werkzeug requests
```

### 3. Run the Application

Start the Flask development server by running:

```bash
python app.py
```

### 4. Access the Blog

Once the server is running, open your browser and go to:

```
http://localhost:7000
```

## Project Structure

The project follows a standard Flask application structure. Below is an overview of the directory tree:

```
flask-blog/
├── app.py                 # Main Flask application entry point
├── blog.db                # SQLite database (created automatically on first run)
├── static/                # Static files (CSS, JS, images)
│   ├── css/               # CSS files for styling
│   ├── js/                # JavaScript files for frontend functionality
│   └── assets/            # Images and other static assets
└── templates/             # HTML templates for rendering pages
    ├── base.html          # Base template with layout structure
    ├── index.html         # Homepage displaying blog posts
    ├── about.html         # About page with information about the blog
    ├── contact.html       # Contact form to get in touch with the admin
    ├── post.html          # Template for displaying individual blog posts
    ├── login.html         # Login form for user authentication
    ├── signup.html        # Signup form for new users
    ├── profile.html       # User profile page to edit details and view posts
    └── footer.html        # Footer include for reuse in all templates
```

## Authentication System

The blog includes a user authentication system using Flask and Werkzeug:

- **SQLite Database**: User data, including passwords and profiles, are stored in the `users` table.
- **Password Hashing**: Passwords are hashed before storing them in the database to ensure security.
- **Session Management**: After logging in, the user session is managed using Flask's session features to keep users logged in across page requests.
- **Email Uniqueness**: The system ensures that each user’s email address is unique.
- **Flash Messages**: After key actions (login, logout, or signup), the app displays messages (success or error) to the user.

### Password Hashing

The password hashing system uses `werkzeug.security`:

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

Passwords are hashed during signup and checked during login.

## Template Structure

The Flask app uses the **Jinja2 templating engine** for rendering HTML pages. The templates are structured as follows:

- `base.html`: This is the base template that defines the overall layout structure of the pages (header, footer, navigation bar). All other templates inherit from this file.
- `index.html`: The homepage displays a list of blog posts fetched dynamically.
- `about.html`: Provides information about the blog platform.
- `contact.html`: Contains a form that sends emails to the administrator when users get in touch.
- `post.html`: Renders individual blog posts, including comments.
- `login.html`: A form to allow existing users to log in.
- `signup.html`: A form for new users to create an account.
- `profile.html`: Displays and allows the user to edit their profile.
- `footer.html`: A small footer section that is reused across all templates.

## Configuration

Before running the application, ensure you configure the following in `app.py`:

### Secret Key

Flask requires a secret key for secure sessions. Set this to a randomly generated string:

```python
app.secret_key = "your-random-secure-key"
```

### Email Settings

To enable the contact form to send emails, update your email configuration in `app.py`:

```python
my_email = "your-email@gmail.com"
my_password = "your-app-password"
```

You can use services like Gmail or any SMTP provider for email functionality.

### API Integration

The blog posts are fetched from an external API endpoint. To change the data source, update the `API_ENDPOINT` variable in `app.py`:

```python
API_ENDPOINT = "your-api-endpoint"
```

This allows you to plug in any API that provides blog posts in the required format.

## Security Considerations

- Passwords are securely hashed using Werkzeug’s `generate_password_hash`
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
