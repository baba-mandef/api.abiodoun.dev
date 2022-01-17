from .settings import *

ALLOWED_HOSTS = ['shadowcompiler.pythonanywhere.com',]
DEBUG = True
TEMPLATES_DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shadowcompiler$default',
        'USER': 'shadowcompiler',
        'PASSWORD': os.environ.get('DBPASS'),
        'HOST': 'shadowcompiler.mysql.pythonanywhere-services.com',
    }
}


CLOUDINARY = {

    'cloud_name': os.environ.get('CLOUDNAME'),
    'api_key': os.environ.get('APIKEY'),
    'api_secret': os.environ.get('APISECRET'),
    'api_proxy': 'http://proxy.server:3128'

}
CLOUDINARY_URL=os.environ.get('CLOUDINARY_URL')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media-henry/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media-henry/')
