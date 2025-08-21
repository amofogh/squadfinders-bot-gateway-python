# Django MongoDB Project

This Django project converts Express/MongoDB models to Django with dual database support.

## Features

- **Dual Database Setup**: SQLite for Django auth, MongoDB via djongo for custom models
- **REST API**: Full CRUD operations for all models using Django REST Framework
- **Admin Interface**: Custom admin with filtering, search, and display options
- **Models**: Player, Message, AIResponse, and AdminUser converted from Mongoose schemas

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
python manage.py migrate --database=mongodb
```

3. Create superuser:
```bash
python manage.py createsuperuser
```

4. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/players/` - Player CRUD operations
- `/api/messages/` - Message CRUD operations  
- `/api/airesponses/` - AI Response CRUD operations
- `/api/adminusers/` - Admin User CRUD operations

## Docker

Build and run with Docker:

```bash
docker build -t django-mongodb-app .
docker run -p 8000:8000 django-mongodb-app
```

## Configuration

Update `django_project/settings.py` with your MongoDB connection details:

```python
DATABASES = {
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'your_mongo_db_name',
        'CLIENT': {
            'host': 'mongodb://your-mongo-host:27017',
        }
    }
}
```