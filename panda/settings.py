import os
import environ
import oscar
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

# Path helper
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

DEBUG = env.bool('DEBUG', default=True)
SQL_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.webfaction.com',
    '.pandaannie.com',
    '.paypal.com',
    'localhost',
    '127.0.0.1',
]

# This is needed for the hosted version of the sandbox
ADMINS = (
    ('Annie Lai', os.environ.get('DEFAULT_FROM_EMAIL', '')),
)
EMAIL_SUBJECT_PREFIX = '[Panda Annie] '
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MANAGERS = ADMINS

# Use a Sqlite database by default
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_NAME', location('db.sqlite')),
        'USER': os.environ.get('DATABASE_USER', None),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', None),
        'HOST': os.environ.get('DATABASE_HOST', None),
        'PORT': os.environ.get('DATABASE_PORT', None),
        'ATOMIC_REQUESTS': True
    }
}

CACHES = {
    'default': env.cache(default='locmemcache://'),
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
USE_TZ = True
TIME_ZONE = 'Europe/London'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

# Includes all languages that have >50% coverage in Transifex
# Taken from Django's default setting for LANGUAGES
gettext_noop = lambda s: s
LANGUAGES = (
    # ('ar', gettext_noop('Arabic')),
    # ('ca', gettext_noop('Catalan')),
    # ('cs', gettext_noop('Czech')),
    # ('da', gettext_noop('Danish')),
    # ('de', gettext_noop('German')),
    # ('en-gb', gettext_noop('British English')),
    # ('el', gettext_noop('Greek')),
    # ('es', gettext_noop('Spanish')),
    # ('fi', gettext_noop('Finnish')),
    ('fr', gettext_noop('French')),
    # ('it', gettext_noop('Italian')),
    # ('ko', gettext_noop('Korean')),
    # ('nl', gettext_noop('Dutch')),
    # ('pl', gettext_noop('Polish')),
    # ('pt', gettext_noop('Portuguese')),
    # ('pt-br', gettext_noop('Brazilian Portuguese')),
    # ('ro', gettext_noop('Romanian')),
    # ('ru', gettext_noop('Russian')),
    # ('sk', gettext_noop('Slovak')),
    # ('uk', gettext_noop('Ukrainian')),
    # ('zh-cn', gettext_noop('Simplified Chinese')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = location("public/media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

if os.environ.get('MAILFROM') is not None and "webfaction" in os.environ.get('MAILFROM'):
    STATIC_ROOT = "/home/nkannielai/webapps/static_media/"
    MEDIA_ROOT = "/home/nkannielai/webapps/media/"
else:
    STATIC_ROOT = location('public/static')
    MEDIA_ROOT = location("public/media")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (
    location('static/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p#!)n1a'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
            oscar.OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                # Oscar specific
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.core.context_processors.metadata',
            ],
            'debug': DEBUG,
        }
    }
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Ensure a valid basket is added to the request instance for every request
    'oscar.apps.basket.middleware.BasketMiddleware',
    # Enable the ProfileMiddleware, then add ?cprofile to any
    # URL path to print out profile details
    #'oscar.profiling.middleware.ProfileMiddleware',
]

ROOT_URLCONF = 'urls'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'oscar': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'oscar.alerts': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': False,
        },

        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },

        # Third party
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sorl.thumbnail': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # 'modeltranslation',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    'paypal',
    'dbbackup',  # django-dbbackup

    # Debug toolbar + extensions
    'debug_toolbar',
    'apps.gateway',     # For allowing dashboard access
    'apps.homepage',
    'widget_tweaks',
] + oscar.get_core_apps(['apps.checkout', 'apps.order', 'apps.shipping', 'apps.partner'])


# Add Oscar's custom auth backend so users can sign in using their email
# address.
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = False

# ====================
# Messages contrib app
# ====================

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': location('whoosh_index'),
    },
}
# Here's a sample Haystack config if using Solr (which is recommended)
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': u'http://127.0.0.1:8983/solr/oscar_latest/',
#        'INCLUDE_SPELLING': True
#    },
#}

# =============
# Debug Toolbar
# =============

# Implicit setup can often lead to problems with circular imports, so we
# explicitly wire up the toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = ['127.0.0.1', '::1']

# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# Meta
# ====
OSCAR_SHOP_NAME = 'Panda'
OSCAR_SHOP_TAGLINE = 'Annie'
OSCAR_HOMEPAGE = reverse_lazy('homepage')
OSCAR_PRODUCTS_PER_PAGE = 8
OSCAR_DEFAULT_CURRENCY = 'EUR'

# email setup
EMAIL_HOST = os.environ.get('EMAIL_HOST')            # 'smtp.webfaction.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # 'nkannielai'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')   # 'annie@pandaannie.com'
EMAIL_USE_TLS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL
OSCAR_FROM_EMAIL = DEFAULT_FROM_EMAIL
DBBACKUP_HOSTNAME = ALLOWED_HOSTS                 # For django-dbbackup app sends failure report

# Hidden Oscar features, e.g. wishlists or reviews
OSCAR_HIDDEN_FEATURES = ["reviews", "wishlists"]

OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': _('Email'),
        'children': [
            {
                'label': _('Broadcast email'),
                'url_name': 'broadcast',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
        ]
    },
]


OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True

# This is added to each template context by the core context processor.  It is
# useful for test/stage/qa sites where you want to show the version of the site
# in the page title.
DISPLAY_VERSION = False


# Order processing
# ================

# Sample order/line status settings. This is quite simplistic. It's like you'll
# want to override the set_status method on the order object to do more
# sophisticated things.
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Complete', 'Cancelled',),
    'Cancelled': (),
    'Complete': (),
}

# This dict defines the line statuses that will be set when an order's status
# is changed
OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Cancelled': 'Cancelled',
    'Complete': 'Shipped',
}

# LESS/CSS
# ========

# We default to using CSS files, rather than the LESS files that generate them.
# If you want to develop Oscar's CSS, then set USE_LESS=True to enable the
# on-the-fly less processor.
USE_LESS = False


# Sentry
# ======

if env('SENTRY_DSN', default=None):
    RAVEN_CONFIG = {'dsn': env('SENTRY_DSN', default=None)}
    LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }
    LOGGING['root']['handlers'].append('sentry')
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')


# Sorl
# ====

THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'
THUMBNAIL_KVSTORE = env(
    'THUMBNAIL_KVSTORE',
    default='sorl.thumbnail.kvstores.cached_db_kvstore.KVStore')
THUMBNAIL_REDIS_URL = env('THUMBNAIL_REDIS_URL', default=None)


# paypal
#PAYPAL_API_USERNAME = 'pandaannielai_api1.gmail.com'
#PAYPAL_API_PASSWORD = 'DQWSQ7FJSABLRJW7'
#PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AdjSq4fSu8rxr1IKTLaMYEnQbyO7'
#PAYPAL_SANDBOX_MODE = False
#paypal sandbox
PAYPAL_API_USERNAME = 'pandaannielai-facilitator_api1.gmail.com'
PAYPAL_API_PASSWORD = 'K59JREM6T3ZT32U6'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AizkRRkMk.O1zdtfpay91.nK5X5N'

if os.environ.get('MAILFROM') is not None and "webfaction" in os.environ.get('MAILFROM'):
    DBBACKUP_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DBBACKUP_STORAGE_OPTIONS = {
        'access_key': os.environ.get('S3_ACCESS_KEY', ''),
        'secret_key':  os.environ.get('S3_SECRET_KEY', ''),
        'bucket_name': 'pandaannie',
        'host': 's3.eu-central-1.amazonaws.com'
    }
    S3_USE_SIGV4 = True
else:
    DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
    DBBACKUP_STORAGE_OPTIONS = {'location': '.'}

DBBACKUP_CONNECTOR_MAPPING = {
    'django.db.backends.sqlite3': 'dbbackup.db.sqlite.SqliteCPConnector',
}

# Django 1.6 has switched to JSON serializing for security reasons, but it does not
# serialize Models. We should resolve this by extending the
# django/core/serializers/json.Serializer to have the `dumps` function. Also
# in tests/config.py
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Try and import local settings which can be used to override any of the above.
try:
    from settings_local import *
except ImportError:
    pass

