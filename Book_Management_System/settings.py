"""
Django settings for Book_Management_System project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目路径的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(8p+ji8uqzhqu1^8di@s1oo=fr29usz)^ycm+rdugor!h*d6mr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 添加应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book.apps.BookConfig',
    'captcha',
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

ROOT_URLCONF = 'Book_Management_System.urls'
# 设置模板文件
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

WSGI_APPLICATION = 'Book_Management_System.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 设置数据库
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'bms',  # 使用数据库的名字,数据库必须手动创建
        'USER': 'root',  # 连接mysql数据库的名字
        'PASSWORD': '270030',  # 用户对应的密码
        'HOST':'localhost',  # 指定mysql数据库所在电脑ip
        'PORT': 3306,  # mysql数据库服务的端口号
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

#LANGUAGE_CODE = 'en-us'  设置时区
LANGUAGE_CODE = 'zh-hans' # 使用中文

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/shanghai' # 中国时间

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# 设置静态文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 引擎
EMAIL_HOST= 'smtp.qq.com'  # 腾讯QQ邮箱的SMTP服务器地址
EMAIL_PORT=25  # smtp服务端口号
EMAIL_HOST_USER='1905471551@qq.com' #发送邮件的qq邮箱
EMAIL_HOST_PASSWORD='miywlpbdxcvkbghg'  # 授权码，进邮箱里面拿
EMAIL_USE_TLS=False # 与SMTP服务器通信时，是否启动TLS链接（安全连接〉，也就是是否加密
EMAIL_FROM='1905471551@qq.com' #同样是你的邮箱，跟上面都是发信者邮箱


