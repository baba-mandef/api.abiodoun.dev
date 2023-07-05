from .settings import *
import dj_database_url

ALLOWED_HOSTS = ['sadih.herokuapp.com']
DEBUG = True
TEMPLATES_DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES['default'] = dj_database_url.config()

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


