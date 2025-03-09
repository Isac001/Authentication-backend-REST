# Import necessary modules
from pathlib import Path
import datetime

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django security features (should be kept secret in production)
SECRET_KEY = 'django-insecure-kf@qpb!f)ron-4!+i6t!ww&kf4z&tow)5(&*tz9=c2tp!)b8m8'

# Enable debug mode (should be set to False in production)
DEBUG = True

# Define the allowed hosts for the application
ALLOWED_HOSTS = [
    "localhost",
    "*"
]

# Installed applications in the Django project
INSTALLED_APPS = [

    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party libraries
    'rest_framework',
    'rest_framework_simplejwt',

    # Custom project apps
    'authentication',
    'simple_crud',
]

# JWT token configuration settings
SIMPLE_JWT = {
    # Access token lifetime (600 minutes = 10 hours)
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=600),

    # Refresh token lifetime (24 hours)
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(hours=24),
}

# Define the default authentication classes for Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Define authentication backends for Django
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Middleware configuration for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Define the root URL configuration for the project
ROOT_URLCONF = 'config.urls'

# Django template engine settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration (using PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database engine
        'NAME': 'auth',  # Database name
        'USER': 'auth',  # Database user
        'PASSWORD': 'root',  # Database password
        'HOST': 'localhost',  # Database host
        'PORT': '5432',  # Database port
    }
}

# Define custom user model for authentication
AUTH_USER_MODEL = 'authentication.User'

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language and time zone settings
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_I18N = True
USE_TZ = True

# Static file configuration (CSS, JavaScript, images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
