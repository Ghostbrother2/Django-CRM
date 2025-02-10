# Django CRM

## Overview
Django CRM is a simple Customer Relationship Management (CRM) system built using Django. It provides basic CRM functionalities such as managing customers, leads, and contacts.

## Features
- User authentication (Login/Logout)
- Manage customers, leads, and contacts
- Admin dashboard for management
- SQLite database support (default, can be changed to MySQL or PostgreSQL)
- Django’s built-in admin panel for quick management

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- pip (Python package manager)
- MySQL (optional, if changing the database backend)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/Ghostbrother2/Django-CRM.git
   cd django-crm
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## Configuration
To change the database from SQLite to MySQL or PostgreSQL, update the `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Change to 'postgresql' for PostgreSQL
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',  # Change to 5432 for PostgreSQL
    }
}
```

## Contribution
Feel free to contribute by forking the repository, making changes, and submitting a pull request.

## License
This project is open-source and available under the MIT License.

