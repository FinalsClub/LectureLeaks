# local settings go here
import dj_database_url
DATABASE['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

ADMIN_MEDIA_PREFIX = '//lectureleaks-static.s3.amazonaws.com/media/'

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = ''
STATIC_URL = '//lectureleaks-static.s3.amazonaws.com/media/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://lectureleaks-static.s3.amazonaws.com/media/'

UPLOAD_ROOT = ''
UPLOAD_HARD = ''
