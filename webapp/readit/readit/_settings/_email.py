import os
from readit._settings import BASE_DIR

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMINS = [('Anton', 'ya.seofox2016@yandex.ru')]
DEFAULT_FROM_EMAIL = 'ya.seofox2016@yandex.ru'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, '../../emails/')

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'seofox123'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
