# Django MongoDB Project

This Django project converts Express/MongoDB models to Django with dual database support.

## Features

- **Dual Database Setup**: SQLite for Django auth, MongoDB via djongo for custom models
- **REST API**: Full CRUD operations for all models using Django REST Framework
- **Admin Interface**: Custom admin with filtering, search, and display options
- **Models**: Player, Message, and AIResponse converted from Mongoose schemas
- **API Documentation**: Swagger/OpenAPI documentation with interactive UI
- **Environment Configuration**: Production-ready settings with .env support

## Setup

1. Copy environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
python manage.py migrate --database=mongodb
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/players/` - Player CRUD operations
- `/api/messages/` - Message CRUD operations  
- `/api/airesponses/` - AI Response CRUD operations

## API Documentation

- `/swagger/` - Interactive Swagger UI
- `/redoc/` - ReDoc documentation
- `/swagger.json` - OpenAPI schema

## Environment Variables

Create a `.env` file with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
MONGO_DB_NAME=players-py
MONGO_HOST=mongodb://user:password@host:port/?authSource=admin
CORS_ALLOW_ALL_ORIGINS=False
```

## Docker

Build and run with Docker:

```bash
docker build -t django-mongodb-app .
docker run -p 8000:8000 django-mongodb-app
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in your `.env` file
2. Configure proper `ALLOWED_HOSTS`
3. Use a strong `SECRET_KEY`
4. Set `CORS_ALLOW_ALL_ORIGINS=False` and configure specific origins
5. Use environment variables for sensitive data
6. Configure proper database backups
7. Set up SSL/HTTPS
8. Configure static file serving