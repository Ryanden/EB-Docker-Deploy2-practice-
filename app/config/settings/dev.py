from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

INSTALLED_APPS += [
    'storages',
    'django_extensions'
]

DEFAULT_FILE_STRAGE = 'config.storages.S3DefaultStorage'

AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = secrets['DATABASES']

