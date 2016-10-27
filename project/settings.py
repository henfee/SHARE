"""
Django settings for share project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from django.utils.log import DEFAULT_LOGGING

from kombu import Queue, Exchange

# Suppress select django deprecation messages
LOGGING = DEFAULT_LOGGING
LOGGING_CONFIG = 'project.log.configure'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'c^0=k9r3i2@kh=*=(w2r_-sc#fd!+b23y%)gs+^0l%=bt_dst0')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', True))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')

AUTH_USER_MODEL = 'share.ShareUser'

JSON_API_FORMAT_KEYS = 'camelize'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'djcelery',
    'guardian',
    'django_filters',
    'django_extensions',
    'oauth2_provider',
    'rest_framework',
    'corsheaders',
    'revproxy',
    'mptt',
    'graphene_django',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # not yet
    # 'allauth.socialaccount.providers.orcid',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
    'osf_oauth2_adapter',

    'share',
    'api',

    'bots.autocurate.person',
    'bots.autocurate.tag',
    'bots.automerge',
    'bots.elasticsearch',

    'providers.au.uow',
    'providers.be.ghent',
    'providers.br.pcurio',
    'providers.ca.lwbin',
    'providers.ca.umontreal',
    'providers.ca.uwo',
    'providers.ch.cern',
    'providers.com.biomedcentral',
    'providers.com.dailyssrn',
    'providers.com.figshare',
    'providers.com.figshare.v2',
    'providers.com.nature',
    'providers.com.peerj',
    'providers.com.peerj.xml',
    'providers.com.peerj.preprints',
    'providers.com.springer',
    'providers.edu.asu',
    'providers.edu.boise_state',
    'providers.edu.calhoun',
    'providers.edu.calpoly',
    'providers.edu.caltech',
    'providers.edu.chapman',
    'providers.edu.citeseerx',
    'providers.edu.cmu',
    'providers.edu.colostate',
    'providers.edu.columbia',
    'providers.edu.csuohio',
    'providers.edu.cuny',
    'providers.edu.cuscholar',
    'providers.edu.dash',
    'providers.edu.digitalhoward',
    'providers.edu.duke',
    'providers.edu.fit',
    'providers.edu.harvarddataverse',
    'providers.edu.huskiecommons',
    'providers.edu.iastate',
    'providers.edu.icpsr',
    'providers.edu.iowaresearch',
    'providers.edu.iu',
    'providers.edu.iwu_commons',
    'providers.edu.kent',
    'providers.edu.krex',
    'providers.edu.mason',
    'providers.edu.mit',
    'providers.edu.mizzou',
    'providers.edu.nku',
    'providers.edu.oaktrust',
    'providers.edu.opensiuc',
    'providers.edu.pcom',
    'providers.edu.pdxscholar',
    'providers.edu.purdue',
    'providers.edu.scholarsarchiveosu',
    'providers.edu.scholarsbank',
    'providers.edu.scholarscompass_vcu',
    'providers.edu.scholarworks_umass',
    'providers.edu.smithsonian',
    'providers.edu.stcloud',
    'providers.edu.texasstate',
    'providers.edu.triceratops',
    'providers.edu.trinity',
    'providers.edu.u_south_fl',
    'providers.edu.udc',
    'providers.edu.udel',
    'providers.edu.uhawaii',
    'providers.edu.uiucideals',
    'providers.edu.ukansas',
    'providers.edu.uky',
    'providers.edu.umassmed',
    'providers.edu.umich',
    'providers.edu.uncg',
    'providers.edu.unl_digitalcommons',
    'providers.edu.upennsylvania',
    'providers.edu.ut_chattanooga',
    'providers.edu.utaustin',
    'providers.edu.utktrace',
    'providers.edu.utuskegee',
    'providers.edu.uwashington',
    'providers.edu.valposcholar',
    'providers.edu.vivo',
    'providers.edu.vtech',
    'providers.edu.wash_state_u',
    'providers.edu.waynestate',
    'providers.edu.wisconsin',
    'providers.edu.wm',
    'providers.edu.wustlopenscholarship',
    'providers.et.edu.addis_ababa',
    'providers.eu.econstor',
    'providers.gov.clinicaltrials',
    'providers.gov.doepages',
    'providers.gov.nih',
    'providers.gov.nist',
    'providers.gov.nodc',
    'providers.gov.nsfawards',
    'providers.gov.pubmedcentral',
    'providers.gov.scitech',
    'providers.gov.usgs',
    'providers.info.spdataverse',
    'providers.io.engrxiv',
    'providers.io.osf',
    'providers.io.osf.preprints',
    'providers.io.osf.registrations',
    'providers.io.socarxiv',
    'providers.io.psyarxiv',
    'providers.org.arxiv',
    'providers.org.arxiv.oai',
    'providers.org.bhl',
    'providers.org.biorxiv',
    'providers.org.biorxiv.rss',
    'providers.org.cogprints',
    'providers.org.crossref',
    'providers.org.datacite',
    'providers.org.datacite.oai',
    'providers.org.dataone',
    'providers.org.dryad',
    'providers.org.elife',
    'providers.org.elis',
    'providers.org.erudit',
    'providers.org.mblwhoilibrary',
    'providers.org.mla',
    'providers.org.mpra',
    'providers.org.ncar',
    'providers.org.neurovault',
    'providers.org.newprairiepress',
    'providers.org.plos',
    'providers.org.repec',
    'providers.org.shareok',
    'providers.org.sldr',
    'providers.org.stepic',
    'providers.org.tdar',
    'providers.org.ucescholarship',
    'providers.org.zenodo',
    'providers.pt.rcaap',
    'providers.ru.cyberleninka',
    'providers.tr.edu.hacettepe',
    'providers.uk.cambridge',
    'providers.uk.lshtm',
    'providers.za.csir',
]


HARVESTER_SCOPES = 'upload_normalized_manuscript upload_raw_data'
USER_SCOPES = 'approve_changesets'

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups',
        'upload_normalized_manuscript': 'Upload Normalized Manuscript',
        'upload_raw_data': 'Upload Raw Data',
        'approve_changesets': 'Approve ChangeSets'
    }
}
SOCIALACCOUNT_ADAPTER = 'osf_oauth2_adapter.views.OSFOAuth2Adapter'
SOCIALACCOUNT_PROVIDERS = \
    {'osf':
        {
            'METHOD': 'oauth2',
            'SCOPE': ['osf.users.profile_read'],
            'AUTH_PARAMS': {'access_type': 'offline'},
            # 'FIELDS': [
            #     'id',
            #     'email',
            #     'name',
            #     'first_name',
            #     'last_name',
            #     'verified',
            #     'locale',
            #     'timezone',
            #     'link',
            #     'gender',
            #     'updated_time'],
            # 'EXCHANGE_TOKEN': True,
            # 'LOCALE_FUNC': 'path.to.callable',
            # 'VERIFIED_EMAIL': False,
            # 'VERSION': 'v2.4'
        }
     }


APPLICATION_USERNAME = 'system'

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'api.renderers.HideNullJSONAPIRenderer',
        # 'rest_framework_json_api.renderers.JSONRenderer',
        # 'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'api.authentication.NonCSRFSessionAuthentication',
    ),
}

GRAPHENE = {
    'SCHEMA': 'share.graphql.schema'
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'share'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', None),
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = os.environ.get('LOGIN_REDIRECT_URL', 'http://localhost:8000/')

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
# else:
INSTALLED_APPS += [
    # 'raven.contrib.django.raven_compat',
]
# RAVEN_CONFIG = {
#   'dsn': os.environ.get('SENTRY_DSN', None),
#   'release': os.environ.get('GIT_COMMIT', None),
# }


# TODO REMOVE BEFORE PRODUCTION
# ALLOW LOCAL USERS TO SEARCH
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# TODO REMOVE BEFORE PRODUCTION

ANONYMOUS_USER_NAME = 'AnonymousUser'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(
        os.path.dirname(__file__),
        'static'
    ),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', 'http://localhost:9200/')
ELASTICSEARCH_INDEX = os.environ.get('ELASTIC_SEARCH_INDEX', 'share')

# Celery Settings

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://'),

CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {}

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_ACKS_LATE = True
CELERY_TRACK_STARTED = True
CELERY_RESULT_PERSISTENT = True
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_LOADER = 'djcelery.loaders.DjangoLoader'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# Celery Queues

DEFAULT_QUEUE = 'celery'
LOW_QUEUE = 'low'
MED_QUEUE = 'med'
HIGH_QUEUE = 'high'

LOW_PRI_MODULES = {
    'share.tasks.HarvesterTask',
}

# Default priority is implicit
# DEFAULT_PRI_MODULES = {
#     'share.tasks.NormalizerTask',
# }

MED_PRI_MODULES = {
    'share.tasks.MakeJsonPatches',
}

HIGH_PRI_MODULES = {
    'share.tasks.BotTask',
    'bots.elasticsearch',
}

CELERY_QUEUES = (
    Queue(LOW_QUEUE, Exchange(LOW_QUEUE), routing_key=LOW_QUEUE,
          consumer_arguments={'x-priority': -10}),
    Queue(DEFAULT_QUEUE, Exchange(DEFAULT_QUEUE), routing_key=DEFAULT_QUEUE,
          consumer_arguments={'x-priority': 0}),
    Queue(MED_QUEUE, Exchange(MED_QUEUE), routing_key=MED_QUEUE,
          consumer_arguments={'x-priority': 20}),
    Queue(HIGH_QUEUE, Exchange(HIGH_QUEUE), routing_key=HIGH_QUEUE,
          consumer_arguments={'x-priority': 30}),
)

CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_ROUTES = ('share.celery.CeleryRouter', )
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(cyan)s[%(asctime)s]%(log_color)s[%(levelname)s][%(name)s]: %(reset)s%(message)s'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'console'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    }
}


# Custom Settings
SITE_ID = 1
PUBLIC_SENTRY_DSN = os.environ.get('PUBLIC_SENTRY_DSN')

EMBER_SHARE_PREFIX = os.environ.get('EMBER_SHARE_PREFIX', 'share' if DEBUG else '')
EMBER_SHARE_URL = os.environ.get('EMBER_SHARE_URL', 'http://localhost:4200').rstrip('/') + '/'
SHARE_API_URL = os.environ.get('SHARE_API_URL', 'http://localhost:8000').rstrip('/') + '/'
SHARE_WEB_URL = os.environ.get('SHARE_WEB_URL', SHARE_API_URL + EMBER_SHARE_PREFIX).rstrip('/') + '/'

OSF_API_URL = os.environ.get('OSF_API_URL', 'https://staging-api.osf.io').rstrip('/') + '/'
DOI_BASE_URL = os.environ.get('DOI_BASE_URL', 'http://dx.doi.org/')

# API KEYS
DATAVERSE_API_KEY = os.environ.get('DATAVERSE_API_KEY')
PLOS_API_KEY = os.environ.get('PLOS_API_KEY')
SPRINGER_API_KEY = os.environ.get('SPRINGER_API_KEY')

import djcelery  # noqa
djcelery.setup_loader()
