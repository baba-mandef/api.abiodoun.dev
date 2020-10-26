from root.settings import *
import dj_database_url

ALLOWED_HOSTS = ['sadih.herokuapp.com', 'henri-dev.tech']
DEBUG = False
TEMPLATES_DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES['default'] = dj_database_url.config()

CLOUDINARY_STORAGE = {

    'CLOUD_NAME': os.environ.get('CLOUDNAME'),
    'API_KEY': os.environ.get('APIKEY'),
    'API_SECRET': os.environ.get('APISECRET')

}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media-henry/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media-henry/')