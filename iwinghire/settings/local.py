# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'iwinghire', 
#         # 'USER': 'swarabadgujar',
#         'USER': 'postgres', 
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1', 
#         'PORT': '5432',
#     }
# }


from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
