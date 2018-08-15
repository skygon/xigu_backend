"""
Django settings for xigu project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5-h1!l8u3lbb=520#7)5%gjqo2n1q7y@qr)#qwp@p7rq93z_p)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.0.106', 'api2-xigu.fang88.com']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',
    'corsheaders',
# user defined apps
    'project.apps.ProjectConfig',
    'user_manage.apps.UserManageConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xigu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'xigu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inner_test_db',   #Name of the DB I have my data in
        'USER': 'root88',
        #'PASSWORD': 'root',
        'PASSWORD': 'fanG882015chinauS',  #Changed for this post
        'HOST': 'rds2m2565y0o4owc90g8.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = '/static/' 
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR,'static'),
#    ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/upload/'


# logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/ubuntu/workspace/skygon/log/xigu/info/info.log',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/ubuntu/workspace/skygon/log/xigu/error/error.log',
        },
    },
    'loggers': {
        'django':{
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': False
        },
        'app_debug':{
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}

# django suit settings
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'XIGUGLOBAL',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'project', 'label': '产品信息管理', 'icon':'icon-cog',
         'models': (
             {'model': 'projectry.Project', 'label': '产品'}, 
             )
        },
        {'app': 'user_manage', 'label': '用户管理', 'icon':'icon-cog',
         'models': (
             {'model': 'user_manage.User', 'label': '用户'}, 
             )
        },
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}
