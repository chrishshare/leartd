"""
Django settings for leartd project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(5st$^=&!89lozp+m)@sn--#@i^zbtfd5+blkoi5y)u+rw)pf4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'favurls.apps.FavurlsConfig',
    'registration',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leartd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'leartd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leartd',
        'USER': 'root',
        'PASSWORD': '@*Zh08241128!*',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = 'staticweb/'

# 日志打印
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
# 设置多媒体文件上传保存路径
MEDIA_URL = "/static/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/")

# session超时策略
SESSION_COOKIE_AGE = 60*60*24*30  # 30分钟。
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# ----------- 邮件发送配置--------------
EMAIL_HOST = 'smtp.163.com'             #SMTP地址
EMAIL_PORT = 465                         #SMTP端口
EMAIL_HOST_USER = 'siyzhou@163.com'     #我自己的邮箱
EMAIL_HOST_PASSWORD = '#zhsy08241128!'  #我的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[leartd]'            #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_SSL= True                    #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
# 管理员站点
SERVER_EMAIL = EMAIL_HOST_USER           #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.


# django-reg-adux settings
ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_DEFAULT_FROM_EMAIL = 'siyzhou@163.com'
REGISTRATION_EMAIL_HTML = True
REGISTRATION_AUTO_LOGIN = True
ACCOUNT_AUTHENTICATED_REGISTRATION_REDIRECTS = True
LOGIN_REDIRECT_URL = '/'
REGISTRATION_USE_SITE_EMAIL = True
REGISTRATION_SITE_USER_EMAIL = REGISTRATION_DEFAULT_FROM_EMAIL
SITE_ID = 1

