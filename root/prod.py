from .settings import *
import pymysql

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "rezogsyk_abiodoun",
        "USER": "rezogsyk_rezogsyk",
        "PASSWORD": os.environ.get('DB_PASS'),
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


DEBUG = os.environ.get('DEBUG')
TEMPLATES_DEBUG = os.environ.get('TEMPLATE_DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['rezolusoft.com', 'www.rezolusoft.com', 'abiodoun.rezolusoft.com', 'api.abiodoun.dev']


STATIC_ROOT = os.path.join('/home/rezogsyk/api.abiodoun.dev/static/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CLOUDINARY = {

    'cloud_name': os.environ.get('CLOUDNAME'),
    'api_key': os.environ.get('APIKEY'),
    'api_secret': os.environ.get('APISECRET'),
    # 'api_proxy': 'http://proxy.server:3128'

}
CLOUDINARY_URL=os.environ.get('CLOUDINARY_URL')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media-henry/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media-henry/')


pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()
