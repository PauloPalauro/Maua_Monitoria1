from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_@876m&g2$*55!90p5cvqfsb)_f07n#33vhp2^3ggabcx#zyjr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'discussion.apps.DiscussionConfig',
    'attendance.apps.AttendanceConfig',
    'quiz.apps.QuizConfig',
    'django_cleanup.apps.CleanupConfig',
    'froala_editor',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'

]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}

JAZZMIN_SETTINGS = {
    "site_header": "Monitoria",
    "site_brand": "Monitoria",
    "site_logo": "images/logo_maua.png",
    "login_logo": "images/logo_maua_2.png",
    "welcome_sign": "Bem vindo ao Perfil Administrativo",
    "copyright": "Mauá Monitoria",
    "changeform_format": "collapsible",
    
    
    "icons": {
        "auth": "",
        "attendance.attendance" : "fas fa-clock",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main.announcement": "fas fa-bullhorn",
        "main.assignment" : "fas fa-book-open",
        "main.course" : "fas fa-chalkboard-teacher",
        "main.department" : "fas fa-school",
        "main.faculty" : "fas fa-glasses",
        "main.material" : "fas fa-users-cog",
        "main.student" : "fas  fa-user-graduate",
        "quiz.question" : "fas fas fa-stream",
        "quiz.quiz" : "fas  fa-file-alt",
        "quiz.studentanswer" : "fas fa-address-book",
    },  
}

ROOT_URLCONF = 'eLMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'eLMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#  < --- Mysql --->

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'elms',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': '',
#     }
# }


#  < --- MongoDb Atlas - Reserva --->

# DATABASES = {
#   'default': {
#        'ENGINE': 'djongo',
#        'NAME': 'Monitoria',
#       'ENFORCE_SCHEMA': False,
#        'CLIENT': {
#            'host': 'mongodb+srv://root:dudis1000@clusterpaulo.mbcm2mx.mongodb.net/',
#            'port': 27017,
#            'username': 'root',
#            'password': 'dudis1000',
#            'authSource': 'admin',
#            'authMechanism': 'SCRAM-SHA-1',
#        }
#    }
# }

#  < --- MongoDb Atlas - Oficial --->


DATABASES = {
    'default':{
        'ENGINE': 'djongo',
        'NAME':'monitoriaIMT',
        'ENFORCE_SCHEMA': False,
        'CLIENT':{
            'host':'mongodb+srv://monitoria:IMTmonitoria@cluster0.vllcn9z.mongodb.net/?retryWrites=true&w=majority'
        }
    }
}


#  < --- MongoDB compass --->

# DATABASES = {
#    'default': {
#        'ENGINE': 'djongo',
#        'NAME': 'Monitoria',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators


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


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
