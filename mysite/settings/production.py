from .base import *
from django.core.management.utils import get_random_secret_key

DEBUG = True # int(os.environ.get("DEBUG", default=1))
#DEBUG = os.getenv("DEBUG", "False") == "True"

SECRET_KEY = 'django-insecure-wt2^elcpvn+a-aa7exnt92ak#l%yozhx+!el^^g1o&z246vyyb'

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ["DJANGO_ALLOWED_HOSTS", "127.0.0.1"]

# try:
#     from .local import *
# except ImportError:
#     pass