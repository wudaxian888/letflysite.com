# -*-coding:utf-8 -*-
# Django settings for letflysite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'letflysite',					   # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': '',
		'PASSWORD': '',
		'HOST': '',						 # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '',						 # Set to empty string for default.
	}
}

AUTH_USER_MODEL = 'user.User'
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/MEDIA_ROOT = '../media/'
MEDIA_ROOT = 'media/'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#	 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_yipymt2kt-13+zk&qoch9*i59khyvu6_43$d%pi(i*7ib@lpe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	  'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'settings.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.wsgi.application'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'templates',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.comments',
	# Uncomment the next line to enable the admin:
	'grappelli',
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	
	#app
	'lblog',
	'core',
	'common',
	'lsite',
	'user',
	'lshare',
		
	# Tools
	'widget_tweaks',
	'captcha',
	'ueditor',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_LEVEL = 'DEBUG'
LOG_FILE_PATH = 'letflysite.log'
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'formatters': {
		'standard': {
			'format': "[%(asctime)s] %(levelname)s [%(name)s:%(pathname)s:%(lineno)s] %(message)s",
			'datefmt': "%d%b%Y %H:%M:%S"
		},
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		},
		'console': {
			'level': LOG_LEVEL,
			'class': 'logging.StreamHandler',
			'formatter': 'standard'
		},
		'file': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': LOG_FILE_PATH,
			'maxBytes': 2 * 1024 * 1024,
			'backupCount': 20,
			'formatter': 'standard',
		},
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		'letflysite': {
			'handlers':	['console', 'file'],
			'level': 'DEBUG',
		},
	}
}

FOCUS_IMAGE_ROOT = 'images/focus'

BLOG_IMAGE_URL = 'images/uploads/'

ACCOUNT_LOCK_BY_ATTEMPTED_COUNT = 5

import os
PHOTO_ROOT = 'images/photos/'
PHOTO_CONF = {
	'limits': {
		'formats': ['.jpg', '.gif', '.jpeg', '.bmp', '.png'],
		'max_file_size': 10 * 1024 * 1024,
		'min_image_size': (600, 350)
	},
	'origin': {
		'dir': os.path.join(PHOTO_ROOT, 'original')
	},
	'dims': {
		's950': {
			'action': 'crop',
			'size': (950, 350),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's950'),
			'quality': 100
		},
		's600': {
			'action': 'crop',
			'size': (600, 350),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's600'),
			'quality': 100
		},
		's350': {
			'action': 'crop',
			'size': (350, 350),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's350'),
			'quality': 100
		},
		's200': {
			'action': 'crop',
			'size': (200, 300),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's200'),
			'quality': 100
		},
		's200c': {
			'action': 'crop',
			'size': (200, 200),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's200c'),
			'quality': 100
		},
		's175d': {
			'action': 'crop',
			'size': (175, 350),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's175d'),
			'quality': 100
		},
		's300h': {
			'action': 'crop',
			'size': (300, 350),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's300h'),
			'quality': 100
		},
		's300l': {
			'action': 'crop',
			'size': (300, 200),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's300l'),
			'quality': 100
		},
		's300s': {
			'action': 'crop',
			'size': (300, 150),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's300s'),
			'quality': 100
		},
		's500': {
			'action': 'crop',
			'size': (500, 440),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's500'),
			'quality': 100
		},
		's250': {
			'action': 'crop',
			'size': (250, 200),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's250'),
			'quality': 100
		},
		's450': {
			'action': 'crop',
			'size': (450, 240),
			'dir': os.path.join(MEDIA_ROOT, PHOTO_ROOT, 's450'),
			'quality': 100
		}
	}
}

BLOG_VISITORS_CACHE_KEY = 'blog:{0}:visitors'
BLOG_VISITORS_CACHE_TIMEOUT = 1 * 1 * 60

INTER_IMAGE_ROOT = 'images/inter/'
INTER_IMAGE_CONF = {
    'limits': {
        'formats': ['.jpg', '.gif', '.jpeg', '.bmp', '.png'],
        'max_file_size': 10 * 1024 * 1024,
        'min_image_size': (950, 280)
    },
    'origin': {
        'dir': os.path.join(INTER_IMAGE_ROOT)
    },
    'dims': {
        'normal': {
            'action': 'scale',
            'size': (950, 0),
            'dir': os.path.join(MEDIA_ROOT, INTER_IMAGE_ROOT),
            'quality': 100
        }
    }
}
INTER_UPLOADED_IMAGE_URL = 'images/inter/uploads/'
INTER_UPLOADED_IMAGE_CONF = {
    'limits': {
        'formats': ('.jpg', '.gif', '.jpeg', '.bmp', '.png'),  # 允许上传的文件类型
        'max_file_size': 5 * 1024 * 1024,                      # 上传的文件大小限制
    },
    'origin': {
        'dir': os.path.join(INTER_IMAGE_ROOT, 'uploads/')
    },
    'dims': {
    },
}
