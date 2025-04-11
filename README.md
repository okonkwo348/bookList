Below is a comprehensive `README.md` file tailored to your project based on the information provided. This includes the features, setup steps, tools used, and additional details inferred from our interactions.

```markdown
# BookList API Project

Welcome to the BookList API project! This is a Django-based RESTful API application designed to manage book-related data and provide user authentication features. The project leverages modern Python tools and libraries to create a robust backend service.

## Table of Contents
- [Features](#features)
- [Technologies and Tools](#technologies-and-tools)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Development and Contribution](#development-and-contribution)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication**: 
  - Login, logout, and registration using `dj-rest-auth`.
  - Integration with `django-allauth` for enhanced account management, including social authentication support.
  - User profile management at `/accounts/profile/`.
- **RESTful API**: 
  - Built with `djangorestframework` to provide a scalable API.
  - Token-based authentication using `rest_framework.authtoken`.
- **User Information Endpoint**: 
  - Custom `/api/user-info/` endpoint returning username, email, and authentication token.
- **Debugging Tools**: 
  - Integration of `django-debug-toolbar` for development debugging.
- **Version Control**: 
  - Managed with Git and hosted on GitHub.

## Technologies and Tools
- **Programming Language**: Python 3.10+
- **Framework**: Django 5.2
- **REST Framework**: `djangorestframework` 3.16.0
- **Authentication**:
  - `dj-rest-auth` 5.x
  - `django-allauth` (for account and social authentication)
  - `rest_framework.authtoken` (for token authentication)
- **Dependencies**:
  - `asgiref` 3.8.1
  - `pytz` 2025.2
  - `sqlparse` 0.5.3
  - `typing-extensions` 4.13.1
  - `tzdata` 2025.2
  - `requests` (for `allauth` social features)
- **Development Tools**:
  - `pip` 24.3.1 (package manager)
  - `pipenv` (virtual environment and dependency management)
  - `setuptools` 75.8.0
  - `wheel` 0.45.1
  - `django-debug-toolbar` 4.3.0
- **Version Control**: Git
- **Code Editor**: Visual Studio Code
- **Operating System**: Windows

## Prerequisites
- Python 3.10 or higher installed.
- Git installed for version control.
- A GitHub account for remote repository hosting.
- Internet connection for installing dependencies and pushing to GitHub.

## Installation and Setup

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/okonkwochi/BookList.git
cd BookList
```

### Step 2: Set Up Virtual Environment
Use `pipenv` to create and activate a virtual environment:
```bash
pipenv install
pipenv shell
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pipenv install django==5.2 djangorestframework==3.16.0 dj-rest-auth django-allauth rest_framework.authtoken django-debug-toolbar pytz==2025.2 sqlparse==0.5.3 typing-extensions==4.13.1 tzdata==2025.2 requests
```

### Step 4: Configure Settings
- Copy `settings.py.example` to `settings.py` (if provided) or edit the existing `settings.py`:
  - Add to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        ...
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth',
        'rest_framework',
        'rest_framework.authtoken',
        'debug_toolbar',
        'BookListAPI',
        ...
    ]
    ```
  - Add to `MIDDLEWARE`:
    ```python
    MIDDLEWARE = [
        ...
        'allauth.account.middleware.AccountMiddleware',
        ...
    ]
    ```
  - Set authentication backends:
    ```python
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )
    ```
  - Set `SITE_ID`:
    ```python
    SITE_ID = 1
    ```
  - Set custom redirect URL:
    ```python
    LOGIN_REDIRECT_URL = '/api/user-info/'
    ACCOUNT_LOGIN_REDIRECT_URL = '/api/user-info/'
    ```

### Step 5: Apply Migrations
Run migrations to set up the database:
```bash
python manage.py migrate
```

### Step 6: Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### Step 7: Set Up Git Remote
Link to the GitHub repository:
```bash
git remote add origin https://github.com/okonkwochi/BookList.git
```

### Step 8: Initialize Git and Push
- Add and commit files:
  ```bash
  git add .
  git commit -m "Initial commit"
  ```
- Push to GitHub:
  ```bash
  git push -u origin main
  ```

## Usage
- Access the API at `http://127.0.0.1:8000/`.
- Use `/api-auth/login/` for the browsable API login (development only).
- Use `/api/rest-auth/login/` for API client login with JSON response.
- Access user info at `/api/user-info/` after authentication.

## API Endpoints
- **`/api-auth/login/`**: DRF browsable API login (redirects to `/api/user-info/` after success).
- **`/api/rest-auth/login/`**: API login endpoint (returns token in JSON).
- **`/api/rest-auth/logout/`**: Logout endpoint.
- **`/api/rest-auth/registration/`**: User registration endpoint.
- **`/api/user-info/`**: Returns authenticated user’s username, email, and token.
- **`/api/book/`**:  Return all the list of books.
-  **`/api/book/id`**: Return detailed of a book.
- **`/admin/`**: Django admin interface.

## Development and Contribution
- **Fork the Repository**: Create your own fork on GitHub.
- **Clone Locally**: Use `git clone` to work on your fork.
- **Create a Branch**: Use `git checkout -b feature-branch-name`.
- **Make Changes**: Implement your features or fixes.
- **Commit Changes**: Use `git commit -m "Description of changes"`.
- **Push to Fork**: Use `git push origin feature-branch-name`.
- **Create Pull Request**: Submit a PR on GitHub for review.
- **Version Control Notes**: Ensure line endings are handled (CRLF on Windows) and resolve submodule issues if present.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details (if applicable).

## Contact
- **Author**: Okonkwo Chi
- **GitHub**: [https://github.com/okonkwochi](https://github.com/okonkwochi)
- **Email**: [your-email@example.com](mailto:your-email@example.com) (replace with your email)

---
