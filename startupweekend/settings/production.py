from .base import *

DEBUG = False

ADMINS = [
    ('Geert Weggemans', 'geert@gweggemans.nl')
]

MANAGERS = ADMINS

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = False

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

X_FRAME_OPTIONS = 'DENY'

DEFAULT_FROM_EMAIL = 'geert@roadmanict.nl'

try:
    from .local import *
except ImportError:
    pass
