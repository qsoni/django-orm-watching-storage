import os
from dotenv import load_dotenv

load_dotenv()
ENGINE = os.getenv('ENGINE')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
ROOT_URLCONF = os.getenv('ROOT_URLCONF')

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = SECRET_KEY

DEBUG = True

ROOT_URLCONF = ROOT_URLCONF

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
