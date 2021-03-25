from .common import *

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]

CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")
