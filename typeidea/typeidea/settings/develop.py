# _*_ coding:utf-8 _*_
__author__ = 'jp'
__date__ = '2020/2/25 10:17'

from .base import * #NOQA 不需要检查pep8规范


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}