import os
from pathlib import Path

# Проекттин папкаларынын жолу
BASE_DIR = Path(__file__).resolve().parent.parent

# Коопсуздук ачкычы
SECRET_KEY = 'django-insecure-l8e$m-qna8@vk7o(der14dwh3s*!(^)yljbohe9pkph14+^w5y'

# Render'ге жүктөгөндө муну False кылсаңыз болот, бирок азырынча True тура берсин
DEBUG = True

# МААНИЛҮҮ: Render сайтыңызды ачышы үчүн '*' деп койдук
ALLOWED_HOSTS = ['*']

# Колдонмолордун тизмеси
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main', # Сиздин колдонмоңуз
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Дизайн үчүн кошулду
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Маалымат базасы (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Тил жана убакыт
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# СТАТИКАЛЫК ФАЙЛДАР (CSS, Сүрөттөр)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Дизайн серверде туура иштеши үчүн Whitenoise жөндөөсү
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'