from pathlib import Path
import os

# Importar python-dotenv para cargar variables de entorno
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-xf$+0c#ba@e9s5=3v1a&ms^_5lnx&w2c@)-52-g45@u$@uh)uc')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,.vercel.app').split(',')


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
    'apps.inicio',
    'apps.contadores',
    'apps.nosotros',
    'apps.beneficios',
    'apps.galeria',
    'apps.ubicacion',
    'apps.preguntas',
    'apps.contacto',
    'apps.whatsapp',
    'apps.cursos',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Configuración para archivos multimedia (imágenes subidas)
MEDIA_URL = '/media/'  # URL pública para acceder a los archivos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta absoluta del sistema de archivos

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración CORS para desarrollo (ajusta para producción)
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:3000,http://127.0.0.1:3000').split(',')

CORS_ALLOW_ALL_ORIGINS = DEBUG  # Solo en desarrollo

CORS_ALLOW_CREDENTIALS = True  # Si usas cookies/auth

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Configuración de base de datos usando variables de entorno
if os.environ.get('DATABASE_URL'):
    # Si existe DATABASE_URL, usar dj-database-url para configurar
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    # Configuración por defecto (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': os.environ.get('DATABASE_NAME', BASE_DIR / 'db.sqlite3'),
        }
    }


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


LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Configuración para archivos estáticos
STATIC_URL = '/static/'  # URL base para archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Carpeta donde se recolectarán los archivos estáticos en producción

# Directorios adicionales donde Django buscará archivos estáticos (aparte de los de cada app)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Carpeta "static" en la raíz del proyecto
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


